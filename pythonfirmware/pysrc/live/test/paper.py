import fonts.fontello
import fonts.basic
from lib.graphics.debug import dump_buffer
from lib.graphics import BufferedCanvas, FontCache
from lib.graphics.font import FontRegistry, FontInfo
import epd
import graphics as graphics
from lib.utils import clear_stats, dump_stats, timed_function, profiled_function, stats_function
from lib.graphics.const import *

d = epd.EPDDisplay(rotation=graphics.ROTATE_90)
c = d.canvas
d.clear(1)

c.draw_rect(0, 0, c.width-1, c.height-1, graphics.BLACK)
c.draw_circle(c.width/2, c.height/2, 20, graphics.BLACK)
c.fill_circle(c.width/2, c.height/2, 15, graphics.BLACK)
c.fill_circle(c.width/2, c.height/2, 5, graphics.WHITE)
c.draw_v_line(c.width/2, c.height/2-20, 40, graphics.BLACK)
c.draw_h_line(c.width/2-20, c.height/2, 40, graphics.BLACK)
d.update_screen(True)


def drawCoord(xdiv, ydiv):
    for x in range(c.width):
        if x % xdiv == 0:
            c.draw_v_line(x, 0, 10, graphics.BLACK)
            c.draw_v_line(x, c.height-10, 10, graphics.BLACK)
    for y in range(c.height):
        if y % ydiv == 0:
            c.draw_h_line(0, y, 10, graphics.BLACK)
            c.draw_h_line(c.width-10, y, 10, graphics.BLACK)


r = FontRegistry()
r.register_font("normal", fonts.basic.u8g2_font_ncenR12_tf)
r.register_font("bold", fonts.basic.u8g2_font_ncenB24_tf)
r.register_font("icons", fonts.fontello.fontello_icons_icon_24)
r.register_font("meteo", fonts.fontello.fontello_meteo_meteo_24)


cache = FontCache(rotation=ROTATE_90)


def enable_cache():
    global cache
    c.set_font_cache(cache)


def disable_cache():
    c.set_font_cache(None)


@stats_function
def drawText(txt, x, y, partial=False, font="normal"):
    c.set_font(r.get(font))
    c.draw_string(txt, x, y)
    ((x0, y0), (x1, y1)) = c.get_bounding_box(txt, x, y)
    # c.draw_rect(x0, y0, x1, y1, 0)
    print("{}x{} - {}x{}".format(x0, y0, x1-x0, y1-y0))
    d.update_screen(True)


enable_cache()
drawText("Hallo Welt", 30, 80)


@profiled_function
@timed_function
def prepCache(seed="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-_+=?/<,>.;:/?!@#$%^&*()\|", font="normal"):
    fi = r.get(font)
    for c in seed:
        glyph = fi.get_glyph(c)
        if glyph:
            cache.store(glyph, rotation=ROTATE_90)


@stats_function
@profiled_function
@timed_function
def prepAll():
    prepCache(font="normal")
    prepCache(font="bold")
    prepCache(font="icons")
    prepCache(font="meteo")


# drawText("Hello-World", 10, 30, True)
# print("------------------")
# clear_stats()
# drawText("G", 10, 40, True, "icons")
# dump_stats()

# Native with print and draw
# ---------------------------
# materialize : 664.977 (1 calls)
# decode_header :  3.848 (3 calls)
# encodeBitL : 367.791 (144 calls)
# draw_string : 920.263 (1 calls)
# get_bounding_box : 10.507 (1 calls)
# update_screen : 930.778 (1 calls)

# Native with encodebitl inlined
# -----------------------------------------------
# materialize : 598.895 (1 calls)
# decode_header :  3.934 (3 calls)
# draw_string : 871.947 (1 calls)
# get_bounding_box : 10.481 (1 calls)
# update_screen : 930.842 (1 calls)

# Native with encodebitl inlined Pixel removed
# -----------------------------------------------
# materialize : 284.448 (1 calls)
# decode_header :  3.630 (3 calls)
# draw_string : 556.944 (1 calls)
# get_bounding_box : 10.326 (1 calls)
# update_screen : 930.956 (1 calls)

# Functional calls
# ---------------------
# materialize : 420.159 (1 calls)
# decode_header :  4.023 (3 calls)
# draw_string : 672.665 (1 calls)
# get_bounding_box : 10.533 (1 calls)
# update_screen : 930.567 (1 calls)


# WITH cache
# 1st call
# ------------
# materialize : 200.369 (1 calls)
# decode_header :  6.575 (4 calls)
# draw_string : 475.840 (1 calls)
# get_bounding_box : 22.431 (2 calls)
# update_screen : 930.985 (1 calls)
# folow calls
# ------------
# get_bounding_box : 22.321 (2 calls)
# decode_header :  5.053 (3 calls)
# update_screen : 930.530 (1 calls)
# draw_string : 263.692 (1 calls)


# prep all
# 5: Function prepAll Time = 38939.894ms
# --> Memory took 58608 Bytes --> total Memory Free(4022608B 3928.33kB)

# 932: Function prepAll Time = 38981.936ms
# --> Memory took 58608 Bytes --> total Memory Free(4022256B 3927.98kB)
# Stats !!
# ------------
# materialize : 33711.092 (309 calls)
# decode_header : 951.925 (618 calls)
# prepCache : 37299.514 (4 calls)
# prepAll : 38981.936 (1 calls)
