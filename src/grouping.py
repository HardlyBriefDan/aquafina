#grouping
# which LEDs to turn on, all of them? every other? bunches
import math
import random

from emulator_backend import Adafruit_NeoPixel

class Grouping():
    
    def __init__(self):
        self.pixels = Adafruit_NeoPixel(20,6,"NEO_GRB + NEO_KHZ800")

    #return a bunch of pixel indexes to be colored
    def bunchGroup(self, startIndex=0, ledCnt=2, allRandom=True):
        if allRandom is True:
            ledCnt = random.randint(ledCnt, math.floor(self.pixels.numPixels() / 2))
            startIndex = random.randint(0, self.pixels.numPixels() - 1)
            print(f"Start Index: {startIndex} ledCnt: {ledCnt}")

        # generate list of indexes
        overCnt = index = 0
        indexes = []
        for i in range(ledCnt):
            if index >= self.pixels.numPixels() - 1 or overCnt > 0:
                index = 0 + overCnt
                overCnt += 1
                indexes.append(index)
            else:
                index = startIndex + i
                indexes.append(index)
        indexes.sort()
        return indexes

    def spacedGroup(self, spacing = 1, startIndex = 0):
        indexes = []
        for index in range(self.pixels.numPixels()):
            if index % (spacing + 1) == 0 and startIndex + index < self.pixels.numPixels():
                indexes.append(index + startIndex)
        indexes.sort()
        return indexes

    def fullStrandGroup(self):
        return self.spacedGroup(spacing=0)
    
    # all random indexes 
    def randomGroup(self, ledCnt=None):
        indexes = []
        if ledCnt is None:
            ledCnt = random.randint(1, self.pixels.numPixels())
        tempIndexes = self.fullStrandGroup()
        for led in range(ledCnt):
            # randIndex = random.randint(0, len(tempIndexes) - 1) # grab a random index
            # indexes = randIndex
            indexes.append(tempIndexes.pop(random.randint(0, len(tempIndexes) - 1)))
        indexes.sort() #this is a test
        return indexes

    # XX - - XX - - XX - - XX - - XX - -
    # X - X - X - X - X
    # X - - X - - X - - X - - X
    def spacedBunchGroup(self, spacing = 2, bunchSize = 2):
        indexes = []
        for bunch in range(bunchSize):
            indexes += (self.spacedGroup(spacing=spacing+1, startIndex=bunch))
        indexes.sort()
        print(indexes)
        return indexes

    # random bunches XX---XXXXX-XX---XXXX
    # TODO implement spacing!
    def randomBunchesGroup(self):
        indexes = []
        numBunches = random.randint(1, math.floor(self.pixels.numPixels()/6))  #arbitrary values
        spacing = random.randint(1, 5)   #arbitrary values

        for bunch in range(numBunches):
            indexes += self.bunchGroup(
                ledCnt=random.randint(2,math.floor(self.pixels.numPixels()/5)),
                startIndex = random.randint(0, self.pixels.numPixels() - 1),
                allRandom=False
            )
        
        indexes.sort()
        indexes = list(dict.fromkeys(indexes))
        print(indexes)



#coloring
#timing
#styling
