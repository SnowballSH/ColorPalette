from color_palette import mix, presets

red = presets.red[0.5]
green = presets.green[-0.4]
blue = presets.blue[0.8]

new = mix([red, green, blue])

print(new)
