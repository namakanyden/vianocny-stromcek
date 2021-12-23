from neopixel import NeoPixel


class SetColorEffect:
    name = "set color"
    description = "Sets all NeoPixels to given color"
    authors = ('mirek <mirek@namakanyden.sk>')
    code = 1009
    
    def run(self, pixels: NeoPixel, color: tuple, **kwargs):
        for i in range(pixels.n):
            pixels[i] = (color[0], color[1], color[2])
        pixels.write()
