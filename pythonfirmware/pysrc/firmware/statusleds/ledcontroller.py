import logging
from machine import Pin
from neopixel import NeoPixel
import globals.pinout as pinout
import uasyncio
import sys
from utils import calc_pos_difference_with_wrap

AREA_ENCODER = 0xff01
AREA_STATUS = 0xff02
AREA_BACKLIGHT = 0xff03
AREA_ALL = 0xff04
LED_POS_LEFT = 0
LED_POS_RIGHT = 1
LED_START_STATUS = 2
LED_END_STATUS = 4
LED_START_BACKLIGHT = 5
LED_END_BACKLIGHT = 12
LED_START_ALL = 0
LED_END_ALL = 12


LOG = logging.getLogger("LED")


class LEDScene:
    def __init__(self):
        self.start_values = []
        self.fps = 20
        pass

    def set_init_values(self,  init_values=None):
        self.start_values = init_values

    def set_fps(self, fps):
        self.fps = fps

    def tick(self, deltaFrames: int, currentValues) -> list:
        pass

    def should_execute(self, delta_frames) -> boolean:
        return True

    def is_finished(self, delta_frames) -> boolean:
        return False

    # Utillity - - Functions
    def convert_to_frames(self, seconds):
        frames = int(seconds*self.fps)
        if frames <= 0:
            frames = 1
            LOG.warning("Limit reached, reset to 1 frame")
        return frames

    def convert_to_frames_ms(self, ms):
        return int((ms/1000)*self.fps)


class LEDSceneIterator(LEDScene):
    def __init__(self):
        super().__init__()

    def tickPixel(self, pixel, deltaFrames, currentValue, initValue):
        pass

    def tick(self, deltaFrames: int, currentValues) -> list:
        if not self.should_execute(deltaFrames):
            return None
        result = []
        for (i, v) in enumerate(currentValues):
            result.append(self.tickPixel(i, deltaFrames, v, self.start_values[i]))
        return result


class LEDSceneItem:
    def __init__(self, region: int, start: int, end: int, init_frames: int, scene: LEDScene, restore_after_exec=False, cur_values=False):
        self.start = start
        self.end = end
        self.region = region
        self.init_frames = init_frames
        self.scene = scene
        self.restore = restore_after_exec
        self.values = cur_values


class LEDController:
    def __init__(self, led=pinout.LED, fps=20):
        pled = Pin(led, Pin.OUT)
        self.pixel = NeoPixel(pled, 13)   # create NeoPixel driver on GPIO0 for 8 pixels
        self.pixel.fill((0, 0, 0))
        self.pixel.write()
        self.fps = fps
        self.current_frame = 0
        uasyncio.get_event_loop().create_task(self.tick())
        self.scenes = []

    def _get_region(self, region):
        if region == AREA_ENCODER:
            return (LED_POS_LEFT, LED_POS_RIGHT)
        elif region == AREA_STATUS:
            return (LED_START_STATUS, LED_END_STATUS)
        elif region == AREA_BACKLIGHT:
            return (LED_START_BACKLIGHT, LED_END_BACKLIGHT)
        elif region == AREA_ALL:
            return (LED_START_ALL, LED_END_ALL)
        else:
            return (region, region)

    def _clean_color(self, color):
        (r, g, b) = color
        if r < 0:
            r = 0
        if g < 0:
            g = 0
        if b < 0:
            b = 0
        return (r, g, b)

    def _write(self, led_start, led_end, values):
        ledNum = led_start
        for value in values:
            self.pixel[ledNum] = self._clean_color(value)
            ledNum += 1
            if ledNum > led_end:
                break

    def _get(self, start, end):
        result = []
        for ledNum in range(start, end+1):
            result.append(self.pixel[ledNum])
        return result

    def _fill(self, led_start, led_end, value):
        for ledNum in range(led_start, led_end+1):
            self.pixel[ledNum] = self._clean_color(value)

    def _remove_scene(self, scene_id):
        scene: LEDSceneItem = self.scenes.pop(scene_id)
        if scene.restore:
            self._write(scene.start, scene.end, scene.values)
            return True
        else:
            return False

    def _tick_scenes(self):
        # TODO only execute first Scene for Area
        remove_ids = []
        dirty = False
        for (index, item) in enumerate((self.scenes)):
            scene: LEDScene = item.scene
            deltaFrames = calc_pos_difference_with_wrap(item.init_frames, self.current_frame)
            if scene.should_execute(deltaFrames):
                results = scene.tick(deltaFrames, self._get(item.start, item.end))
                self._write(item.start, item.end, results)
                dirty = True
            if scene.is_finished(deltaFrames):
                remove_ids.append(index)
        for i in reversed(remove_ids):
            if self._remove_scene(i):
                dirty = True
        if dirty:
            self.pixel.write()

    def fill(self, led, value):
        (start, stop) = self._get_region(led)
        self._fill(start, stop, value)
        self.pixel.write()

    def write(self, led, values):
        (start, stop) = self._get_region(led)
        if isinstance(values, list):
            self._write(start, stop, values)
        elif isinstance(values, tuple):
            self._fill(start, stop, values)
        self.pixel.write()

    def add_scene(self, region, scene: LEDScene, restore_after_execution=True):
        # TODO Only allow areas
        (start, stop) = self._get_region(region)
        initValues = self._get(start, stop)
        item = LEDSceneItem(region, start, stop, self.current_frame, scene, restore_after_execution, initValues)
        item.scene.set_fps(self.fps)
        item.scene.set_init_values(initValues)
        self.scenes.insert(0, item)
        LOG.debug("Added Scene {} to region {} ({},{})".format(scene, region, start, stop))
        return item

    async def tick(self):
        while True:
            self.current_frame += 1
            self._tick_scenes()
            await uasyncio.sleep_ms(1000//self.fps)
