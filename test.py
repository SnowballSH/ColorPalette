from color_palette import mixing, presets, picker

red = presets.red[0.5]
green = presets.green[-0.4]
blue = presets.blue[0.8]

new = mixing.mix([red, green, blue, picker.pick()])

print(new)
