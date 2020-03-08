
from color_generators import ColorGenerators

class CustomEffects():

    def __init__(self, pixel_strand):
        self.pixels = pixel_strand

    def flash_effect(self, spacing=1, cycle=1):
        # flash every other pixel
        cg = ColorGenerators()

        for times in range(cycle):
            #color = cg.randColor()
            color = cg.genRGBfromHSL(cg.HUES['GREEN'])
            print(times, color)
            for i in range(self.pixels.numPixels()):
                if(i % spacing == 0):
                    self.pixels.setPixelColor(i, self.pixels.Color(
                        color[0],
                        color[1],
                        color[2]
                    ))
            self.pixels.show()
            self.pixels.delay(100) 
            self.pixels.clear()
            self.pixels.show()
            self.pixels.delay(100)

    def lightning_effect(self, effect_time=0, cycle=0):
        # flash every other pixel
        cg = ColorGenerators()
        delay = 100
        delay_deg = .15
        color = cg.randColor()
        for j in range(6):
            for i in range(self.pixels.numPixels()):
                if(i % 2 == 0):
                    self.pixels.setPixelColor(i, self.pixels.Color(
                        color[0],
                        color[1],
                        color[2]
                    ))
            tempD = delay - (j * delay_deg * delay)
            if(tempD < 0):
                tempD = 0
            self.pixels.show()
            self.pixels.delay(tempD) 
            self.pixels.clear()
            self.pixels.show()
            self.pixels.delay(tempD)      