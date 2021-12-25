from neopixel import NeoPixel


class ClearEffect:
    name = "clear"
    description = "Turns the neopixel off by setting it's color to black"
    authors = ('mirek <mirek@namakanyden.sk>')
    code = 1001
    
    def run(self, pixels: NeoPixel, **kwargs):
        for i in range(pixels.n):
            pixels[i] = (0, 0, 0)
        pixels.write()
