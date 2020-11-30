
# This file is executed on every boot (including wake-boot from deepsleep)
# import esp
# esp.osdebug(None)
# import webrepl
# webrepl.start()
#
import hal
import gc
from utils import clean_memory, create_repeat_task
from fonts import fontello, fu, u8glib
import uasyncio
import logging

logging.basicConfig(level=logging.DEBUG)
logging.getLogger("Base").debug("Logging enabled")
logging.basicConfig(level=logging.WARNING)

print("Initializing HAL")
hal.init()

print("register Fonts")
hal.fonts.register_font("7seg", u8glib.u8g2_font_7Segments_26x42_mn)
hal.fonts.register_font("small", fu.u8g2_font_fur11_tf)
hal.fonts.register_font("normal", fu.u8g2_font_fur14_tf)
hal.fonts.register_font("large", fu.u8g2_font_fur25_tf)
hal.fonts.register_font("small_bold", fu.u8g2_font_fur11_tf)
hal.fonts.register_font("normal_bold", fu.u8g2_font_fur14_tf)
hal.fonts.register_font("large_bold", fu.u8g2_font_fur25_tf)
hal.fonts.register_font("meteo", fontello.fontello_meteo_meteo_12)
hal.fonts.register_font("meteo_large", fontello.fontello_meteo_meteo_24)
hal.fonts.register_font("meteo_huge", fontello.fontello_meteo_meteo_32)
hal.fonts.register_font("icon", fontello.fontello_icons_icon_12)
hal.fonts.register_font("icon", fontello.fontello_icons_icon_24)

print("Start wifi")
hal.init_wifi()

print("Initializing HAL...done")
clean_memory(True)
