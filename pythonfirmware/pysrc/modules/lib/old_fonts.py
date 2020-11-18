import json
import lib.utils as utils
from lib.utils import timed_function


class GlyphBuffer:
    def __init__(self, w, h):
        self.buffer = bytearray(((w*h)//8)+1)
        self.width = w
        self.height = h

    def fill(self, color):
        val = 0
        if (color == 1):
            val = 0xff
        for l in range(len(self.buffer)):
            self.buffer[l] = val

    def setPixel(self, x, y, color):
        idx = y*self.width+x
        byteIdx = idx//8
        bitIdx = idx % 8
        color &= 1
        v = color << bitIdx
        self.buffer[byteIdx] = self.buffer[byteIdx] | v

    def getPixel(self, x, y):
        idx = y*self.width+x
        byteIdx = idx//8
        bitIdx = idx % 8
        block = self.buffer[byteIdx]
        bit = (block >> bitIdx) & 0b1
        return bit

    def iterate(self, w=0, h=0):
        if w == 0:
            w = self.width
        if h == 0:
            h = self.height
        for y in range(h):
            for x in range(w):
                yield (x, y, self.getPixel(x, y))

    def dump(self, w=0, h=0):
        lasty = 0
        line = " 0:"
        for (x, y, c) in self.iterate(w, h):
            if y != lasty:
                lasty = y
                line += "\n"+"{0:2d}".format(y)+":"
            if(c == 1):
                line += "x"
            else:
                line += "."

        return line


class FontInfo:
    def readWord(self, pos):
        d = self.font[pos]
        d <<= 8
        d += self.font[pos+1]
        return d

    def __init__(self, font):
        self.glyphCount = font[0]
        self.bbxMode = font[1]
        self.bitsPer0 = font[2]
        self.bitsPer1 = font[3]
        self.bitsPerCharWidth = font[4]
        self.bitsPerCharHeight = font[5]
        self.bitsPerCharX = font[6]
        self.bitsPerCharY = font[7]
        self.bitsPerDeltaX = font[8]
        self.maxCharWidth = utils.convertUint8ToInt8(font[9])
        self.maxCharHeight = utils.convertUint8ToInt8(font[10])
        self.xOffset = utils.convertUint8ToInt8(font[11])
        self.yOffset = utils.convertUint8ToInt8(font[12])
        self.ascentA = utils.convertUint8ToInt8(font[13])
        self.descentG = utils.convertUint8ToInt8(font[14])
        self.ascentPara = utils.convertUint8ToInt8(font[15])
        self.descentPara = utils.convertUint8ToInt8(font[16])
        self.startUpperA = (font[17] << 8)+font[18]
        self.startLowerA = (font[19] << 8)+font[20]
        self.startUnicode = (font[21] << 8)+font[22]
        self.font = font

    def getGlyph(self, char):
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
                pos += self.readWord(unicodeTable)
                lastEncoding = self.readWord(unicodeTable+2)
                unicodeTable += 4
                if (lastEncoding >= code):
                    break
            while True:
                currentEncoding = self.readWord(pos)
                if (code == currentEncoding):
                    return pos+3
                else:
                    pos += self.font[pos+2]
                    if pos+1 >= len(self.font):
                        break  # reached the end, no filler

        return None


class FontGlyphDecoder:
    def __init__(self, font: FontInfo, glyphStart):
        self.fontInfo = font
        self.startPos = glyphStart
        self.currentBytePos = glyphStart
        self.currentBitPos = 0

    def getUnsignedBits(self, cnt):

        bpos = self.currentBitPos
        pos = self.currentBytePos

        bposFinal = bpos+cnt
        v = 0

        if bposFinal < 8:
            v = self.fontInfo.font[pos]
            v >>= bpos
            v &= (1 << cnt)-1
        else:
            v = self.fontInfo.font[pos]
            pos += 1
            v += self.fontInfo.font[pos] << 8
            v >>= bpos
            v &= (1 << cnt)-1
        bpos = bposFinal % 8
        self.currentBytePos = pos
        self.currentBitPos = bpos
        return v

    def getSignedBits(self, cnt):
        v = self.getUnsignedBits(cnt)
        d = 1
        cnt -= 1
        d <<= cnt
        v -= d
        return v

    def encodeBitL(self, drawFunc, len):
        while len > 0:
            if drawFunc:
                drawFunc(self.posX, self.posY, self)
            len -= 1
            self.posX += 1
            if self.posX >= self.glyphWidth:
                self.posY += 1
                self.posX = 0

    def decode(self):
        fi = self.fontInfo
        w = self.glyphWidth = self.getUnsignedBits(
            fi.bitsPerCharWidth)
        h = self.glyphHeight = self.getUnsignedBits(
            fi.bitsPerCharHeight)
        x = self.getSignedBits(fi.bitsPerCharX)
        y = self.getSignedBits(fi.bitsPerCharY)
        d = self.getSignedBits(fi.bitsPerDeltaX)
        self.targetX = x
        self.targetY = h+y
        return self

    def draw(self, drawFunc1, drawFunc0):

        fi = self.fontInfo
        w = self.glyphWidth = self.getUnsignedBits(
            fi.bitsPerCharWidth)
        h = self.glyphHeight = self.getUnsignedBits(
            fi.bitsPerCharHeight)
        x = self.getSignedBits(fi.bitsPerCharX)
        y = self.getSignedBits(fi.bitsPerCharY)
        d = self.getSignedBits(fi.bitsPerDeltaX)
        self.targetX = x
        self.targetY = h+y
        self.posX = 0
        self.posY = 0

        while True:
            a = self.getUnsignedBits(fi.bitsPer0)
            b = self.getUnsignedBits(fi.bitsPer1)
            while True:
                self.encodeBitL(drawFunc0, a)
                self.encodeBitL(drawFunc1, b)
                if (self.getUnsignedBits(1) == 0):
                    break
            if(self.posY >= self.glyphHeight):
                break
        return self

    def dump(self):
        return self.fontInfo.glyphBuffer.dump(self.glyphWidth, self.glyphHeight)

    def dump_pixel(self, x, y):
        for (x0, y0, c) in self.fontInfo.glyphBuffer.iterate(self.glyphWidth, self.glyphHeight):
            y0 += y-self.targetY+1
            x0 += self.targetX+x
            yield (x0, y0, c)
