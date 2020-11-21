
from .utils import *
from lib.utils import timed_function, traced_function
import micropython

from ... import graphics


class Glyph:
    def __init__(self, fi: FontInfo, startpos: int, code: int):
        self.font = fi
        self.glyphPos = startpos
        # Offset is in bits
        self.code = code
        self.reader = BitstreamReader(fi.font, startpos*8)
        self.decode_header()

    @traced_function
    def decode_header(self):
        self.width = self.reader.read_unsigned_bits(
            self.font.bitsPerCharWidth)
        self.height = self.reader.read_unsigned_bits(
            self.font.bitsPerCharHeight)
        x = self.reader.read_signed_bits(self.font.bitsPerCharX)
        y = self.reader.read_signed_bits(self.font.bitsPerCharY)
        d = self.reader.read_signed_bits(self.font.bitsPerDeltaX)
        self.upper_left_x = x
        self.upper_left_y = self.height+y
        self.offset_x = x
        self.offset_y = y
        self.delta_x = d
        return self

#    @traced_function
    def encodeBitL(self, v, canvas, len, tracker):
        while len > 0:
            canvas.pixel(tracker.x, tracker.y, v)
            len -= 1
            tracker.step()

    @traced_function
    def materialize(self, canvas: graphics.DrawRoutines, transparent=False):
        # need to repositioning, could do a direct offset but this would be additional cost to maintain.
        # reading some header bits is reasonable fast, so no problem here
        self.reader.move_to(self.glyphPos*8)
        self.decode_header()

        # decoding into buffer or canvas.
        # Assuming the canvas is B/W with White for background and Black for FG
        # this asumes a pixel() function exists
        # and the canvase is 0/0 on uper-left with start pos needed to shift down
        # correction for shifting later in the target drawing. This is a plain buffer!
        posX = 0
        posY = 0
        rle = self.reader

        if not transparent:
            canvas.clear(graphics.WHITE)

        tracker = PixelPointer(0, 0, self.width, self.height)

        while True:
            # RLE on R0 and R1
            a = rle.read_unsigned_bits(self.font.bitsPer0)
            b = rle.read_unsigned_bits(self.font.bitsPer1)
            while True:
                # skip 0
                len = a
                while len > 0:
                    len -= 1
                    tracker.step()
                len = b
                while len > 0:
                    canvas.pixel(tracker.x, tracker.y, 0)
                    len -= 1
                    tracker.step()

                if rle.read_unsigned_bits(1) == 0:
                    break
            if tracker.is_overflow():
                break
        return self


class FontInfo:
    def __init__(self, name: string, font):
        self.glyphCount = font[0]
        self.bbxMode = font[1]
        self.bitsPer0 = font[2]
        self.bitsPer1 = font[3]
        self.bitsPerCharWidth = font[4]
        self.bitsPerCharHeight = font[5]
        self.bitsPerCharX = font[6]
        self.bitsPerCharY = font[7]
        self.bitsPerDeltaX = font[8]
        self.maxCharWidth = convertUint8ToInt8(font[9])
        self.maxCharHeight = convertUint8ToInt8(font[10])
        self.xOffset = convertUint8ToInt8(font[11])
        self.yOffset = convertUint8ToInt8(font[12])
        self.ascentA = convertUint8ToInt8(font[13])
        self.descentG = convertUint8ToInt8(font[14])
        self.ascentPara = convertUint8ToInt8(font[15])
        self.descentPara = convertUint8ToInt8(font[16])
        self.startUpperA = read_word_from_bytes(font, 17)
        self.startLowerA = read_word_from_bytes(font, 19)
        self.startUnicode = read_word_from_bytes(font, 21)
        self.font = font
        self.name = name

    def search_glyph(self, char):
        code = ord(char)
        pos = 23  # Jump FontInfo Block
        if (code <= 255):
            if code >= ord('a'):
                pos += self.startLowerA
            elif code >= ord('A'):
                pos += self.startUpperA
            while True:
                if self.font[pos+1] == 0:
                    break
                if self.font[pos] == code:
                    return pos+2  # skip glyph size and actual code, return offset to glyph
                pos += self.font[pos+1]  # advanced glyph size
        else:  # unicode
            pos += self.startUnicode
            unicodeTable = pos
            while True:
                pos += read_word_from_bytes(self.font, unicodeTable)
                lastEncoding = read_word_from_bytes(self.font, unicodeTable+2)
                unicodeTable += 4
                if (lastEncoding >= code):
                    break
            while True:
                if pos+1 >= len(self.font):
                    break  # reached the end, no filler
                currentEncoding = read_word_from_bytes(self.font, pos)
                if (code == currentEncoding):
                    return pos+3
                else:
                    pos += self.font[pos+2]
                    if pos+1 >= len(self.font):
                        break  # reached the end, no filler

        return None

    def get_glyph(self, c: char):
        code = self.search_glyph(c)
        if code == None:
            return None
        else:
            return Glyph(self, code, ord(c))


class FontRegistry:
    def __init__(self):
        self.fonts = {}

    def register_font(self, name: string, font_buffer: bytes):
        fi = FontInfo(name, font_buffer)
        self.fonts[name] = fi

    def get(self, name: string):
        if not name in self.fonts.keys():
            return None
        else:
            return self.fonts[name]
