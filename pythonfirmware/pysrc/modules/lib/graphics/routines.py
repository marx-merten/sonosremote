import framebuf
# from lib.fonts import FontInfo, FontGlyphDecoder
from lib.utils import timed_function
from .font import FontInfo
from .const import *


class DrawRoutines:
    def __init__(self, w, h):
        self.width = w
        self.height = h
        self.error_msg = False

    def pixel(self, x, y, color):
        if not self.error_msg:
            print("Pixel draw not supported, please check implementation.")
            self.error_msg = True
        return self

    def clear(self, color):
        self.fill_rect(0, 0, self.width, self.height, color)

    def draw_line(self, x0, y0, x1, y1, color):
        # Bresenham algorithm
        dx = abs(x1 - x0)
        sx = 1 if x0 < x1 else -1
        dy = -abs(y1 - y0)
        sy = 1 if y0 < y1 else -1
        err = dx + dy
        while((x0 != x1) and (y0 != y1)):
            self.pixel(x0, y0, color)
            if (2 * err >= dy):
                err += dy
                x0 += sx
            if (2 * err <= dx):
                err += dx
                y0 += sy
        return self

    def draw_h_line(self, x, y, width, color):
        for i in range(x, x + width):
            self.pixel(i, y, color)
        return self

    def draw_v_line(self, x, y, height, color):
        for i in range(y, y + height):
            self.pixel(x, i, color)
        return self

    def draw_rect(self, x0, y0, x1, y1, color):
        min_x = x0 if x1 > x0 else x1
        max_x = x1 if x1 > x0 else x0
        min_y = y0 if y1 > y0 else y1
        max_y = y1 if y1 > y0 else y0
        self.draw_h_line(
            min_x, min_y, max_x - min_x + 1, color)
        self.draw_h_line(
            min_x, max_y, max_x - min_x + 1, color)
        self.draw_v_line(min_x,
                         min_y, max_y - min_y + 1, color)
        self.draw_v_line(max_x,
                         min_y, max_y - min_y + 1, color)
        return self

    def fill_rect(self,  x0, y0, x1, y1, color):
        min_x = x0 if x1 > x0 else x1
        max_x = x1 if x1 > x0 else x0
        min_y = y0 if y1 > y0 else y1
        max_y = y1 if y1 > y0 else y0
        for i in range(min_x, max_x + 1):
            self.draw_v_line(
                i, min_y, max_y - min_y + 1, color)
        return self

    def draw_circle(self, x, y, radius, color):
        # Bresenham algorithm
        x_pos = -radius
        y_pos = 0
        err = 2 - 2 * radius
        # if (x >= self.width or y >= self.height):
        #     return
        while True:
            self.pixel(x - x_pos, y + y_pos, color)
            self.pixel(x + x_pos, y + y_pos, color)
            self.pixel(x + x_pos, y - y_pos, color)
            self.pixel(x - x_pos, y - y_pos, color)
            e2 = err
            if (e2 <= y_pos):
                y_pos += 1
                err += y_pos * 2 + 1
                if(-x_pos == y_pos and e2 <= x_pos):
                    e2 = 0
            if (e2 > x_pos):
                x_pos += 1
                err += x_pos * 2 + 1
            if x_pos > 0:
                break
        return self

    def fill_circle(self,  x, y, radius, color):
        # Bresenham algorithm
        x_pos = -radius
        y_pos = 0
        err = 2 - 2 * radius
        # if (x >= self.width or y >= self.height):
        #     return
        while True:
            self.pixel(x - x_pos, y + y_pos, color)
            self.pixel(x + x_pos, y + y_pos, color)
            self.pixel(x + x_pos, y - y_pos, color)
            self.pixel(x - x_pos, y - y_pos, color)
            self.draw_h_line(
                x + x_pos, y + y_pos, 2 * (-x_pos) + 1, color)
            self.draw_h_line(
                x + x_pos, y - y_pos, 2 * (-x_pos) + 1, color)
            e2 = err
            if (e2 <= y_pos):
                y_pos += 1
                err += y_pos * 2 + 1
                if(-x_pos == y_pos and e2 <= x_pos):
                    e2 = 0
            if (e2 > x_pos):
                x_pos += 1
                err += x_pos * 2 + 1
            if x_pos > 0:
                break
        return self

    def get_window(self, x, y, w, h):
        return WindowCanvas(self, x, y, w, h)

    def set_font(self, font: FontInfo):
        self.current_font = font

    @timed_function
    def get_bounding_box(self, txt: string, x, y, kerning=0):
        upper = y
        lower = y
        right = x
        for c in txt:
            glyph = self.current_font.get_glyph(c)
            if glyph:
                upper = min(upper, y-glyph.upper_left_y)
                lower = max(lower, y-glyph.offset_y)
                right += glyph.width+glyph.upper_left_x
            else:
                glyph = self.current_font.get_glyph('A')
                if glyph:
                    upper = min(upper, y-glyph.upper_left_y)
                    lower = max(lower, y-glyph.offset_y)
                    right += glyph.width+glyph.upper_left_x
                else:
                    upper = min(upper, y-self.current_font.ascentA)
                    lower = max(lower, y-self.current_font.descentG)
                    right += self.current_font.maxCharWidth
        return((x, upper), (right, lower))

    @timed_function
    def draw_string(self, txt: string, x, y, inverse=False, kerning=0, transparent=False):
        ((x0, y0), (x1, y1)) = self.get_bounding_box(txt, x, y, kerning)
        if not transparent:
            self.fill_rect(x0, y0, x1, y1, BLACK if inverse else WHITE)
        str_x = x
        for c in txt:
            glyph = self.current_font.get_glyph(c)
            if glyph:
                dc = self.get_window(
                    str_x, y-glyph.upper_left_y, glyph.width, glyph.height)
                glyph.materialize(dc)
                str_x += glyph.width+glyph.upper_left_x


class WindowCanvas (DrawRoutines):
    def __init__(self, display: DrawRoutines, x, y, w, h):
        self.display = display
        self.translate_x = x
        self.translate_y = y
        self.width = w
        self.height = h
        self.error_msg = False

    def pixel(self, x, y, color):
        if (x >= self.width or y >= self.height):
            return
        self.display.pixel(x+self.translate_x, y+self.translate_y, color)

    # Stupid implementation, if needed need to be overwritten with a more perfomend version
    def clear(self, color=0):
        self.display.fill_rect(0, 0, self.width-1, self.height-1, color)
