import lib.graphics.debug as gdebug
import lib.graphics as graphics
d = graphics.BufferedCanvas(25, 200)
d.rotate(graphics.ROTATE_90)
d.clear()
d.draw_rect(20, 0, 25, 4, 1)


def dump():
    gdebug.dump_buffer(d, d.width, d.height)


dump()
