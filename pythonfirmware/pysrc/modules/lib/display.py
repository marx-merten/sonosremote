import lib.epaper2in9 as epaper
import globals.pinout as pinout
from machine import SPI, Pin
import framebuf
from lib.fonts import FontInfo, FontGlyphDecoder
from lib.utils import timed_function

BLACK = 0
WHITE = 1
EPD_WIDTH = 128
EPD_HEIGHT = 296
ROTATE_0 = 0
ROTATE_90 = 1
ROTATE_180 = 2
ROTATE_270 = 3


class DrawRoutines:
    def __init__(self, w, h):
        self.width = w
        self.height = h

    def set_pixel(self, x, y, color):
        if not self.error_msg:
            print("Pixel draw not supported, please check implementation.")
            self.error_msg = True
        return self

    def draw_line(self, x0, y0, x1, y1, color):
        # Bresenham algorithm
        dx = abs(x1 - x0)
        sx = 1 if x0 < x1 else -1
        dy = -abs(y1 - y0)
        sy = 1 if y0 < y1 else -1
        err = dx + dy
        while((x0 != x1) and (y0 != y1)):
            self.set_pixel(x0, y0, color)
            if (2 * err >= dy):
                err += dy
                x0 += sx
            if (2 * err <= dx):
                err += dx
                y0 += sy
        return self

    def draw_h_line(self, x, y, width, color):
        for i in range(x, x + width):
            self.set_pixel(i, y, color)
        return self

    def draw_v_line(self, x, y, height, color):
        for i in range(y, y + height):
            self.set_pixel(x, i, color)
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
            self.set_pixel(x - x_pos, y + y_pos, color)
            self.set_pixel(x + x_pos, y + y_pos, color)
            self.set_pixel(x + x_pos, y - y_pos, color)
            self.set_pixel(x - x_pos, y - y_pos, color)
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
            self.set_pixel(x - x_pos, y + y_pos, color)
            self.set_pixel(x + x_pos, y + y_pos, color)
            self.set_pixel(x + x_pos, y - y_pos, color)
            self.set_pixel(x - x_pos, y - y_pos, color)
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

    def set_font(self, font):
        self.font = FontInfo(font)
        return self

    def get_text_boundingbox(self, text, x, y):
        max_x = 0
        max_y = 0
        min_y = 0
        for c in text:
            gcode = self.font.search_glyph(c)
            if (gcode != None):
                glyph = FontGlyphDecoder(self.font, gcode).decodeHeader()
                lower_y = glyph.targetY-glyph.glyphHeight
                if min_y > lower_y:
                    min_y = lower_y
                if max_y < glyph.targetY:
                    max_y = glyph.targetY
                max_x += glyph.targetX+glyph.glyphWidth
            else:
                min_y = self.font.descentG
                max_y = self.font.ascentA
                max_x += self.font.maxCharWidth
        return (x, y-max_y, x+max_x, y-min_y)

    @timed_function
    def draw_text(self, text, x, y, color=0, bgColor=1, transparent=False, kerning=0):
        print(len(self.rawBuffer))
        (x0, y0, x1, y1) = self.get_text_boundingbox(text, x, y)
        if not transparent:
            self.fill_rect(x0, y0, x1, y1, bgColor)

        # Set Start pos
        char_x = x
        char_y = y
        print(len(self.rawBuffer))

        for c in text:
            glyph = self.font.get_glyph(c)
            print(c)
            print(len(self.rawBuffer))

            # gcode = self.font.search_glyph(c)

            # if (gcode != None):
            if glyph:
                print(len(self.rawBuffer))
                glyph.draw(char_x, char_y, self, color, bgColor)
                print(len(self.rawBuffer))

                # advance to next char
                char_x = glyph.targetX+glyph.glyphWidth+kerning
            else:
                (x0, y0, x1, y1) = self.get_text_boundingbox('A', char_x, char_y)
                self.draw_rect(x0, y0, x1, y1, color)
                char_x = x1+kerning
        return self


class Window (DrawRoutines):
    def __init__(self, display, x, y, w, h):
        self.display = display
        self.translate_x = x
        self.translate_y = y
        self.width = w
        self.height = h
        self.error_msg = False

    def set_pixel(self, x, y, color):
        if (x >= self.width or y >= self.height):
            return
        self.display.set_pixel(x+self.translate_x, y+self.translate_y, color)


class Display (DrawRoutines):
    def wake(self):
        self.ePaper.init()
        # probably reset will work as  well

    def sleep(self):
        self.ePaper.sleep()

    def clear(self, color=WHITE):
        self.rawFB.fill(color)
        self.update_screen()

    def update_screen(self, partial=False):
        self.wake()
        if partial:
            self.ePaper.set_lut(epaper.EPD.LUT_PARTIAL_UPDATE)

        self.ePaper.set_frame_memory(
            self.rawBuffer, 0, 0, EPD_WIDTH, EPD_HEIGHT)
        self.ePaper.display_frame()
        self.ePaper.sleep()

    def frame(self):
        return self.rawFB

    def __init__(self, spi_channel=2, sck_pin=18, mosi_pin=23,
                 miso_pin=19, cs_pin=pinout.DISP_CS, dc_pin=pinout.DISP_DC,
                 rst_pin=pinout.DISP_RST, busy_pin=pinout.DISP_BUSY):

        super(Display, self).__init__(EPD_WIDTH, EPD_HEIGHT)

        spi = SPI(spi_channel, baudrate=2000000, polarity=0, phase=0,
                  sck=Pin(sck_pin), mosi=Pin(mosi_pin), miso=Pin(miso_pin))

        cs = Pin(cs_pin)
        dc = Pin(dc_pin)
        rst = Pin(rst_pin)
        busy = Pin(busy_pin)

        self.rotate = ROTATE_0

        e = epaper.EPD(spi, cs, dc, rst, busy)
        e.init()
        self.ePaper = e
        # use a frame buffer
        # 128 * 296 / 8 = 4736 - thats a lot of pixels
        self.rawBuffer = bytearray(128 * 296 // 8)
        self.rawFB = framebuf.FrameBuffer(
            self.rawBuffer, EPD_WIDTH, EPD_HEIGHT, framebuf.MONO_HLSB)
        self.ePaper.set_frame_memory(
            self.rawBuffer, 0, 0, EPD_WIDTH, EPD_HEIGHT)
        self.sleep()

    def set_rotate(self, rotate):
        if (rotate == ROTATE_0):
            self.rotate = ROTATE_0
            self.width = EPD_WIDTH
            self.height = EPD_HEIGHT
        elif (rotate == ROTATE_90):
            self.rotate = ROTATE_90
            self.width = EPD_HEIGHT
            self.height = EPD_WIDTH
        elif (rotate == ROTATE_180):
            self.rotate = ROTATE_180
            self.width = EPD_WIDTH
            self.height = EPD_HEIGHT
        elif (rotate == ROTATE_270):
            self.rotate = ROTATE_270
            self.width = EPD_HEIGHT
            self.height = EPD_WIDTH

    def set_pixel(self, x, y, color):
        if (x < 0 or x >= self.width or y < 0 or y >= self.height):
            return
        if (self.rotate == ROTATE_0):
            self.set_absolute_pixel(x, y, color)
        elif (self.rotate == ROTATE_90):
            point_temp = x
            x = EPD_WIDTH - y
            y = point_temp
            self.set_absolute_pixel(x, y, color)
        elif (self.rotate == ROTATE_180):
            x = EPD_WIDTH - x
            y = EPD_HEIGHT - y
            self.set_absolute_pixel(x, y, color)
        elif (self.rotate == ROTATE_270):
            point_temp = x
            x = y
            y = EPD_HEIGHT - point_temp
            self.set_absolute_pixel(x, y, color)

    def set_absolute_pixel(self,  x, y, color):
        # To avoid display orientation effects
        # use EPD_WIDTH instead of self.width
        # use EPD_HEIGHT instead of self.height
        if (x < 0 or x >= EPD_WIDTH or y < 0 or y >= EPD_HEIGHT):
            return
        self.rawFB.pixel(x, y, color)

    def translate(self, x, y):
        x0 = x
        y0 = y
        if (self.rotate == ROTATE_90):
            x0 = EPD_WIDTH - y
            y0 = x
        elif (self.rotate == ROTATE_180):
            x0 = EPD_WIDTH - x
            y0 = EPD_HEIGHT - y
        elif (self.rotate == ROTATE_270):
            x0 = y
            y0 = EPD_HEIGHT - x
        return (x0, y0)

    def blit(self, fb, x, y):
        (x0, y0) = self.translate(x, y)
        print("Draw Blit to {:d}:{:d}".format(x0, y0))
        self.rawFB.blit(fb, x0, y0)
