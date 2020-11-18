import lib.epaper2in9 as epaper
import globals.pinout as pinout
from machine import SPI, Pin
import lib.graphics as graphics
from lib.utils import timed_function

EPD_WIDTH = 128
EPD_HEIGHT = 296


class EPDDisplay:
    def wake(self):
        self.ePaper.init()
        # probably reset will work as  well

    def sleep(self):
        self.ePaper.sleep()

    def clear(self, color=graphics.WHITE):
        self.canvas.clear(color)
        self.update_screen()

    @timed_function
    def update_screen(self, partial=False):
        self.wake()
        if partial:
            self.ePaper.set_lut(epaper.EPD.LUT_PARTIAL_UPDATE)

        self.ePaper.set_frame_memory(
            self.canvas.buffer, 0, 0, EPD_WIDTH, EPD_HEIGHT)
        self.ePaper.display_frame()
        self.ePaper.sleep()

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
