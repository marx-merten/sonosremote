import globals.pinout as pinout

from epd import EPDDisplay
from graphics import BufferedCanvas, FontCache
from graphics.const import *
from graphics.font import FontInfo, FontRegistry
from statusleds import *
from asyncWifiManager import WifiManager


import utime

from rotary_irq_esp import RotaryIRQ, Rotary
import globals.pinout as pinout

# Important hardware pointers

# Fonts and Graphics
# ------------------
display: EBDDisplay = None
canvas: BufferedCanvas = None
font_cache: FontCache = None
fonts: FontRegistry = None
leds = None

# Todo
buttons = None
sound = None
encoder: Rotary = None
wifi = None


def init():
    global display, canvas, font_cache, fonts, buttons, sound, encoder, leds
    leds = LEDController()
    leds.fill(AREA_ALL, (0, 0, 0))
    leds.fill(AREA_STATUS, (5, 3, 10))

    display = EPDDisplay(rotation=ROTATE_90)
    canvas = display.canvas
    fonts = FontRegistry()
    font_cache = FontCache(rotation=ROTATE_90)
    canvas.set_font_cache(font_cache)


def preload():
    """ Optional preload and cache warming, will be switchable in teh final version.
        not calling this will likely not change and functions but ma slow down operations """
    display.clear(WHITE)
    canvas.clear(WHITE)
    canvas.set_font(fonts.get("normal"))
    canvas.draw_string("Preloading Fonts", 10, 40)
    plFonts = ["small", "normal", "large", "small_bold", "normal_bold", "large_bold", "meteo", "meteo_large", "meteo_huge"]
    totalCount = len(plFonts)
    count = 0
    for fname in plFonts:
        canvas.fill_rect(0, canvas.height-20, (canvas.width/len(plFonts))*count, canvas.height, BLACK)
        count += 1
        display.update_screen(True)
        fi = fonts.get(fname)
        if fi:
            for c in ASCII_SEED:
                glyph = fi.get_glyph(c)
                if glyph:
                    font_cache.store(glyph, rotation=ROTATE_90)
        canvas.fill_rect(0, canvas.height-20, (canvas.width/len(plFonts))*count, canvas.height, BLACK)
        display.update_screen(True)


def init_wifi():
    wifi = WifiManager()
    wifi.start_network()

# WifiManager.start_managing()
