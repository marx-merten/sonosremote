import framebuf
# from lib.fonts import FontInfo, FontGlyphDecoder
from lib.utils import timed_function


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

    # def set_font(self, font):
    #     self.font = FontInfo(font)
    #     return self

    # def get_text_boundingbox(self, text, x, y):
    #     max_x = 0
    #     max_y = 0
    #     min_y = 0
    #     for c in text:
    #         gcode = self.font.search_glyph(c)
    #         if (gcode != None):
    #             glyph = FontGlyphDecoder(self.font, gcode).decodeHeader()
    #             lower_y = glyph.targetY-glyph.glyphHeight
    #             if min_y > lower_y:
    #                 min_y = lower_y
    #             if max_y < glyph.targetY:
    #                 max_y = glyph.targetY
    #             max_x += glyph.targetX+glyph.glyphWidth
    #         else:
    #             min_y = self.font.descentG
    #             max_y = self.font.ascentA
    #             max_x += self.font.maxCharWidth
    #     return (x, y-max_y, x+max_x, y-min_y)

    # @timed_function
    # def draw_text(self, text, x, y, color=0, bgColor=1, transparent=False, kerning=0):
    #     print(len(self.rawBuffer))
    #     (x0, y0, x1, y1) = self.get_text_boundingbox(text, x, y)
    #     if not transparent:
    #         self.fill_rect(x0, y0, x1, y1, bgColor)

    #     # Set Start pos
    #     char_x = x
    #     char_y = y
    #     print(len(self.rawBuffer))

    #     for c in text:
    #         glyph = self.font.get_glyph(c)
    #         print(c)
    #         print(len(self.rawBuffer))

    #         # gcode = self.font.search_glyph(c)

    #         # if (gcode != None):
    #         if glyph:
    #             print(len(self.rawBuffer))
    #             glyph.draw(char_x, char_y, self, color, bgColor)
    #             print(len(self.rawBuffer))

    #             # advance to next char
    #             char_x = glyph.targetX+glyph.glyphWidth+kerning
    #         else:
    #             (x0, y0, x1, y1) = self.get_text_boundingbox('A', char_x, char_y)
    #             self.draw_rect(x0, y0, x1, y1, color)
    #             char_x = x1+kerning
    #     return self
