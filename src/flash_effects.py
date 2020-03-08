import math
import random

from color_generators import ColorGenerators
from grouping import Grouping

class FlashEffects():

    def __init__(self, pixel_strand):
        self.pixels = pixel_strand

    # send a list of colors
    def singleColorFlash(self, spacing=0, timeOn=100, color=None, useHues=False):
        cg = ColorGenerators()
        if color is None and not useHues:
            color = cg.randColor()
        elif color is None and useHues:
            color = cg.randColorFromHues()
        for i in range(self.pixels.numPixels()):
            if(i % (spacing + 1) == 0):
                self.pixels.setPixelColor(i, self.pixels.Color(
                    color[0],
                    color[1],
                    color[2]
                ))
        self.pixels.show()
        self.pixels.delay(timeOn) 
        self.pixels.clear()
        self.pixels.show()
    
    # just turns the pixels on
    def full_strand_flash(self, color=None, random_color=True):
        grouping = Grouping(self.pixels)
        color_gens = ColorGenerators()
        if color is None:
            color = color_gens.randColorFromHues()
        indexes = grouping.full_strand_flash()
        for index in range(indexes):
            self.pixels[index] = color

    def strandFlash(self, color, spacing = 0, timeOn = 100):
        for i in range(self.pixels.numPixels()):
            if(i % (spacing + 1) == 0):
                self.pixels.setPixelColor(i, self.pixels.Color(
                    color[0],
                    color[1],
                    color[2]
                ))
        self.pixels.show()
        self.pixels.delay(timeOn) 
        self.pixels.clear()
        self.pixels.show()

    def groupFlash(self, ledCnt=0, timeOn = 500, startIndex=0, endIndex=0, isRandom=True):
        if isRandom is True:
            ledCnt = random.randint(2, math.floor(self.pixels.numPixels() / 2))
        
        startIndex = random.randint(0, self.pixels.numPixels() - 1)
        print(f"Start Index: {startIndex} ledCnt: {ledCnt}")
        color = (243,204,255)

        overCnt = 0
        for i in range(ledCnt):
            index = startIndex + i
            # 5 pixels
            # index = 6 = (5 + 2)
            if index > self.pixels.numPixels() - 1:
                index = 0 + overCnt
                overCnt += 1
            else:
                index = startIndex + i

            print(f"Index: {index}")
            self.pixels.setPixelColor(index, self.pixels.Color(
                color[0],
                color[1],
                color[2]
            ))
        self.pixels.show()
        self.pixels.delay(timeOn) 
        self.pixels.clear()
        self.pixels.show()




    def lighting(self, strikes=7, color=None):

        startDelay = delay = 100
        # default purplish color
        if color is None:
            color = (243,204,255)

        for strike in range(strikes):
            self.Flash(color, timeOn=delay)
            self.pixels.delay(30)
            delay_percent = 1/ math.pow(math.e, strike)
            delay = delay - (strike * delay_percent * startDelay)
            print(delay)