import hal
from graphics.const import *
from statusleds import ledcontroller, SceneMorph, SceneReplay
import uasyncio
from utils import clean_memory, create_repeat_task

print("Main Operation started")

hal.canvas.clear(WHITE)
hal.canvas.draw_line(0, 0, hal.canvas.width, hal.canvas.height-40, BLACK)
hal.canvas.draw_line(0, hal.canvas.height-40, hal.canvas.width, 0, BLACK)
hal.display.update_screen()
hal.display.clear(WHITE)

print("Startup Finished")


# setup async system
def main():
    uasyncio.create_task(create_repeat_task(clean_memory, 60000, True))
    uasyncio.get_event_loop().run_forever()


def loop():
    uasyncio.get_event_loop().run_forever()


fade = SceneMorph((0, 0, 0), steps=5, runtime_s=0.5)
hal.leds.add_scene(ledcontroller.AREA_STATUS, fade)

frames = [(500, [(20, 40, 10)]),
          (200, [(50, 10, 0)])]
sr = SceneReplay(frames)
hal.leds.add_scene(ledcontroller.AREA_ENCODER, sr)


# Start main loop
# needs to be the last one in the row
main()
