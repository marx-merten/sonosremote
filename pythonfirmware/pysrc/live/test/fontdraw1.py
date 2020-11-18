import fonts.fontello
import fonts.basic
from lib.graphics.debug import dump_buffer
from lib.graphics import BufferedCanvas
from lib.graphics.font import FontRegistry, FontInfo
import lib.graphics.debug as gdebug
import lib.graphics as graphics
d = graphics.BufferedCanvas(25, 200)
d.rotate(graphics.ROTATE_90)
d.clear()
d.draw_rect(20, 0, 25, 4, 1)


r = FontRegistry()
r.register_font("normal", fonts.basic.u8g2_font_ncenR08_tf)
f = r.get("normal")
d.set_font(f)
d.clear(1)
d.draw_string("HI World", 30, 12)


def dump():
    gdebug.dump_buffer(d, d.width, d.height)


dump()
