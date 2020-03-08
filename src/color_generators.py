import random
import math

class ColorGenerators():

    HUES = {
        'RED' : 0,
        'YELLOW' : 60,
        'GREEN' : 120,
        'CYAN' : 180,
        'BLUE' : 240,
        'MAGENTA' : 300,
    }

    # returns rgb value
    def random_color_RGB(self):
        return (random.randint(0,255), random.randint(0,255), random.randint(0,255))

    # returns random rgb from randomly selected HUE
    def random_color_hue(self):
        index = random.randint(0, len(self.HUES)-1)
        hueKey = list(self.HUES.keys())[index]
        return self.gen_RGB_from_HSL(self.HUES[hueKey])

    def gen_RGB_from_HSL(self, hue):
        hue = hue
        saturation = random.randint(40, 100) / 100  # arbitrary values
        lightness = random.randint(30, 70) / 100    # arbitrary values
        print(f"Hue: {hue}, Sat: {saturation}, Lght: {lightness}")
        C = (1 - abs(2 * lightness - 1)) * saturation
        X = C * (1 - abs((hue/60)%2-1))
        m = lightness - C/2
        print(f"C: {C}, X: {X}, m: {m}")
        
        #(C,X,0)
        if hue < 60:
            return (
                math.floor(((C + m)*255)),
                math.floor(((X + m)*255)),
                math.floor(m*255),
            )
        elif hue >= 60 and hue < 120:
            return (
                math.floor(((X + m)*255)),
                math.floor(((C + m)*255)),
                math.floor(m*255),
            )
        elif hue >= 120 and hue < 180:
            return (
                math.floor(m*255),
                math.floor(((C + m)*255)),
                math.floor(((X + m)*255)),
            )
        elif hue >= 180 and hue < 240:
            return (
                math.floor(m*255),
                math.floor(((X + m)*255)),
                math.floor(((C + m)*255)),
            )
        elif hue >= 240 and hue < 300:
            return (
                math.floor(((X + m)*255)),
                math.floor(m*255),
                math.floor(((C + m)*255)),
            )
        elif hue >= 300 and hue < 360:
            return (
                math.floor(((C + m)*255)),
                math.floor(m*255),
                math.floor(((X + m)*255)),
            )