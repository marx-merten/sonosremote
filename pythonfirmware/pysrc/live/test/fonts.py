from lib.graphics.font import FontRegistry, FontInfo
from lib.graphics import BufferedCanvas, ASCII_SEED
from lib.graphics.debug import dump_buffer
import fonts.basic
import fonts.fontello

r = FontRegistry()
r.register_font("normal_12", fonts.basic.u8g2_font_ncenR24_tf)
r.register_font("bold_12", fonts.basic.u8g2_font_ncenB12_tf)
r.register_font("icons", fonts.fontello.fontello_icons_icon_24)
f = r.get("normal_12")
f
u = r.get("icons")
u.search_glyph('\ue70d')
f.search_glyph('i')


bb = BufferedCanvas(40, 40)
bb.clear(1)
dump_buffer(bb, 40, 40)


def testChar(font: FontInfo, c):
    print("Font max:{:d}x{:d}".format(font.maxCharWidth, font.maxCharHeight))
    glyph = font.get_glyph(c)
    if glyph:
        print("Glyph Size:{:d}x{:d}".format(glyph.width, glyph.height))
        print("Glyph UL:{:d}x{:d}".format(
            glyph.upper_left_x, glyph.upper_left_y))
        print("Glyph YOffset:{:d}".format(glyph.offset_y))

        glyph.materialize(bb)
        dump_buffer(bb, glyph.width, glyph.height)


def findMissing(font: FontInfo, search=ASCII_SEED):
    for c in search:
        g = font.get_glyph(c)
        if not g:
            print("Code Missing in Fone {} --[{}]".format(font.name, c))
