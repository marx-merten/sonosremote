from statusleds.scenes import *
from statusleds.utils import *
from statusleds import ledcontroller
from hal import leds


def simpleMorph():
    global leds
    frames = [(500, [(20, 40, 10)]),
              (200, [(50, 10, 0)])]
    sr = SceneReplay(frames)
    leds.add_scene(ledcontroller.AREA_ENCODER, sr)


def policeMorph(ste=4):
    global leds
    c_in = morph_linear(8, (50, 0, 0), (0, 0, 50))
    c_out = morph_linear(8, (0, 0, 50), (50, 0, 0))

    scene = [(1000, 1, c_in),
             (200, ste, c_out),
             (1000, 1, c_out),
             (200, ste, c_in)]
    frames = morph_scene_linear(scene)
    for f in frames:
        print(f)
    sr = SceneReplay(frames, 10)
    leds.add_scene(ledcontroller.AREA_BACKLIGHT, sr)
