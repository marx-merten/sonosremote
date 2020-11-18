import framebuf
# from lib.fonts import FontInfo, FontGlyphDecoder
from lib.utils import timed_function
from .routines import DrawRoutines
BLACK = 0
WHITE = 1

ROTATE_0 = 0
ROTATE_90 = 1
ROTATE_180 = 2
ROTATE_270 = 3


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


class BufferedCanvas (DrawRoutines):
    def __init__(self, width, height, rotation=ROTATE_0):
        self.buffer_width = width
        self.buffer_height = height
        self.rotate(rotation)
        bcount = width * height // 8
        if(bcount % 8 > 0):
            bcount += height
        print(bcount)

        self.buffer = bytearray(bcount)

        self.framebuffer = framebuf.FrameBuffer(
            self.buffer, width, height, framebuf.MONO_HLSB)

    def clear(self, color=0):
        self.framebuffer.fill(color)

    def rotate(self, rotation):
        self.rotation = rotation
        if (rotation == ROTATE_0):
            self.width = self.buffer_width
            self.height = self.buffer_height
        elif (rotation == ROTATE_90):
            self.width = self.buffer_height
            self.height = self.buffer_width
        elif (rotation == ROTATE_180):
            self.width = self.buffer_width
            self.height = self.buffer_height
        elif (rotation == ROTATE_270):
            self.width = self.buffer_height
            self.height = self.buffer_width

    #  if (x < 0 or x >= self.width or y < 0 or y >= self.height):
    #         return
    #     if (self.rotate == ROTATE_0):
    #         self.set_absolute_pixel(x, y, color)
    #     elif (self.rotate == ROTATE_90):
    #         point_temp = x
    #         x = EPD_WIDTH - y
    #         y = point_temp
    #         self.set_absolute_pixel(x, y, color)
    #     elif (self.rotate == ROTATE_180):
    #         x = EPD_WIDTH - x
    #         y = EPD_HEIGHT - y
    #         self.set_absolute_pixel(x, y, color)
    #     elif (self.rotate == ROTATE_270):
    #         point_temp = x
    #         x = y
    #         y = EPD_HEIGHT - point_temp
    #         self.set_absolute_pixel(x, y, color)

    def translate(self, x, y):
        if self.rotation == ROTATE_0:
            return(x, y)
        elif self.rotation == ROTATE_90:
            return(self.buffer_width-y-1, x)
        elif self.rotation == ROTATE_180:
            return(self.buffer_width-x-1, self.buffer_height-y-1)
        elif self.rotation == ROTATE_270:
            return(y, self.buffer_height-x-1)

    def pixel(self, x, y, color=None):
        (x0, y0) = self.translate(x, y)
        if color != None:
            if (x < 0 or x >= self.width or y < 0 or y >= self.height):
                return
            self.buffer_pixel(x0, y0, color)
        else:
            return self.framebuffer.pixel(x0, y0)

    def buffer_pixel(self, x, y, color):
        self.framebuffer.pixel(int(x), int(y), color)

    def get_window(self, x, y, w, h):
        return WindowCanvas(self, x, y, w, h)
