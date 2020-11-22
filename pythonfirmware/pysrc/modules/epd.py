import epaper2in9 as epaper
import globals.pinout as pinout
from machine import SPI, Pin
import graphics
from utils import timed_function, traced_function

EPD_WIDTH = 128
EPD_HEIGHT = 296

BLACK = 0
WHITE = 1


class EPDDisplay:
    def wake(self):
        self.ePaper.init()
        # probably reset will work as  well

    def sleep(self):
        self.ePaper.sleep()

    def clear(self, color=graphics.WHITE):
        self.canvas.clear(color)
        self.update_screen()

    @traced_function
    def update_screen(self, partial=False):
        self.wake()
        if partial:
            self.ePaper.set_lut(epaper.EPD.LUT_PARTIAL_UPDATE)

        self.ePaper.set_frame_memory(
            self.canvas.buffer, 0, 0, EPD_WIDTH, EPD_HEIGHT)
        self.ePaper.display_frame()
        self.ePaper.sleep()

    # @traced_function
    # def update_screen_area(self, x0, y0, x1, y1, partial=True):
    #     # self.canvas.translate(x0,y0)
    #     (tx0, ty0) = self.canvas.translate(x0, y0)
    #     (tx1, ty1) = self.canvas.translate(x1, y1)
    #     posNW_x = min(tx0, tx1)
    #     posNW_y = min(ty0, ty1)
    #     posSE_x = max(tx0, tx1)
    #     posSE_y = max(ty0, ty1)
    #     x = posNW_x
    #     y = posNW_y
    #     w = posSE_x-posNW_x
    #     h = posSE_y-posNW_y

    #     x &= 0xfff8
    #     w |= 0x0007
    #     w += 1
    #     leftByte = x//8
    #     rowSkipBytes = EPD_WIDTH//8
    #     rangeBytes = w//8
    #     startPosByte = y*rowSkipBytes
    #     pos = startPosByte+leftByte
    #     targetbuffer = bytearray(rangeBytes*h)
    #     targetpos = 0
    #     for y0 in range(h):
    #         for y1 in range(rangeBytes):
    #             targetbuffer[targetpos] = self.canvas.buffer[pos]
    #             targetpos += 1
    #             pos += 1
    #         pos += rowSkipBytes-rangeBytes
    #     # content transfered
    #     self.wake()
    #     if partial:
    #         self.ePaper.set_lut(epaper.EPD.LUT_PARTIAL_UPDATE)

    #     self.ePaper.set_frame_memory(
    #         targetbuffer, x, y, w, h)
    #     self.ePaper.display_frame()
    #     self.ePaper.sleep()

    def frame(self):
        return self.rawFB

    def __init__(self, spi_channel=2, sck_pin=18, mosi_pin=23,
                 miso_pin=19, cs_pin=pinout.DISP_CS, dc_pin=pinout.DISP_DC,
                 rst_pin=pinout.DISP_RST, busy_pin=pinout.DISP_BUSY, rotation=graphics.ROTATE_0):

        spi = SPI(spi_channel, baudrate=2000000, polarity=0, phase=0,
                  sck=Pin(sck_pin), mosi=Pin(mosi_pin), miso=Pin(miso_pin))

        cs = Pin(cs_pin)
        dc = Pin(dc_pin)
        rst = Pin(rst_pin)
        busy = Pin(busy_pin)

        e = epaper.EPD(spi, cs, dc, rst, busy)
        e.init()
        self.ePaper = e
        self.canvas = graphics.BufferedCanvas(
            EPD_WIDTH, EPD_HEIGHT, rotation)
        self.ePaper.set_frame_memory(
            self.canvas.buffer, 0, 0, EPD_WIDTH, EPD_HEIGHT)
        self.sleep()
