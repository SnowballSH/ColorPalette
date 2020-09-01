from color_palette import color, mix

red = color.Colour((255, 0, 0))
green = color.Colour((0, 255, 0))
blue = color.Colour((0, 0, 255))

new = mix.mix([red, green, blue])

print(new)

