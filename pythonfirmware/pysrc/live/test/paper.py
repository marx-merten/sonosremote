import fonts.fontello
import fonts.basic
from lib.graphics.debug import dump_buffer
from lib.graphics import BufferedCanvas
from lib.graphics.font import FontRegistry, FontInfo
import epd
import lib.graphics as graphics

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
r.register_font("bold", fonts.basic.u8g2_font_ncenB12_tf)
r.register_font("icons", fonts.fontello.fontello_icons_icon_24)
r.register_font("meteo", fonts.fontello.fontello_meteo_meteo_24)


def drawText(txt, x, y, partial=False, font="normal"):
    c.clear(1)
    c.set_font(r.get(font))
    c.draw_string(txt, x, y)
    d.update_screen(partial)


drawText("Hello-World", 10, 30, True)
drawText("G", 10, 40, True, "icons")
