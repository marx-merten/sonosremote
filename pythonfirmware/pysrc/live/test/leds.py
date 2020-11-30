from statusleds.scenes import *
from statusleds import ledcontroller
import hal
import main


def simpleMorph():
    fade = SceneMorph((0, 0, 0), steps=5, runtime_s=0.5)
    hal.leds.add_scene(ledcontroller.AREA_STATUS, fade)

    frames = [(500, [(20, 40, 10)]),
              (200, [(50, 10, 0)])]
    sr = SceneReplay(frames)
    hal.leds.add_scene(ledcontroller.AREA_ENCODER, sr)
    main.loop()
