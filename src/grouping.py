# Grouping class has several methods that return index values of whatever led
# strand length is passed in

import math
import random

class Grouping():
    
    def __init__(self,pixel_strand):
        self.pixels =  pixel_strand
        self.pixel_count = len(self.pixels) # to eliminate the number of times we call for its size

    #returns 1 bunch group ---XXXX-------
    def bunch_group(self, startIndex=0, ledCnt=2, allRandom=True):
        if allRandom is True:
            ledCnt = random.randint(ledCnt, math.floor(self.pixel_count / 2))
            startIndex = random.randint(0, self.pixel_count - 1)
            print(f"Start Index: {startIndex} ledCnt: {ledCnt}")

        # generate list of indexes
        overCnt = index = 0
        indexes = []
        for i in range(ledCnt):
            if index >= self.pixel_count - 1 or overCnt > 0:
                index = 0 + overCnt
                overCnt += 1
                indexes.append(index)
            else:
                index = startIndex + i
                indexes.append(index)
        indexes.sort()
        return indexes

    # returns list of indexes that are evenly spaced
    # X-X-X-X-X-X
    def spaced_group(self, spacing = 1, startIndex = 0):
        indexes = []
        for index in range(self.pixel_count):
            if index % (spacing + 1) == 0 and startIndex + index < self.pixel_count:
                indexes.append(index + startIndex)
        indexes.sort()
        return indexes

    # returns list of every index
    def full_strand_group(self):
        indexes = []
        for index in range(self.pixel_count):
            indexes.append(index)
        return indexes
    
    # returns list of random index values
    def random_group(self, ledCnt=None):
        indexes = []
        if ledCnt is None:
            ledCnt = random.randint(1, self.pixel_count)
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
    # does not work as intended.....
    def spaced_bunch_group(self, spacing = 2, bunchSize = 2):
        indexes = []
        for bunch in range(bunchSize):
            indexes += (self.spacedGroup(spacing=spacing+1, startIndex=bunch))
        indexes.sort()
        print(indexes)
        return indexes

    # random bunches XX---XXXXX-XX---XXXX
    # TODO implement spacing!
    def random_bunches_group(self):
        indexes = []
        numBunches = random.randint(1, math.floor(self.pixel_count/6))  #arbitrary values
        spacing = random.randint(1, 5)   #arbitrary values

        for bunch in range(numBunches):
            indexes += self.bunchGroup(
                ledCnt=random.randint(2,math.floor(self.pixel_count/5)),
                startIndex = random.randint(0, self.pixel_count - 1),
                allRandom=False
            )
        
        indexes.sort()
        indexes = list(dict.fromkeys(indexes))
        print(indexes)