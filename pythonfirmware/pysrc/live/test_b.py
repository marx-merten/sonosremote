import fonts.basic
import fonts.fontello
import lib.display
d = lib.display.Display()
d.set_rotate(1)
d.clear()
d.set_font(fonts.fontello.fontello_meteo_icon_24)
d.draw_text(fonts.fontello.GLYPH_METEO_CLOUD_FLASH_INV,
            100, 50).update_screen(True)
# d.set_font(fonts.basic.u8g2_font_ncenB12_tf)
# d.draw_text("Hello", 20, 20)
# d.update_screen(True)
