from color_palette import color

red = color.Colour((23, 12, 72))
print(red)
print(red.red)
print(red.green)
print(red.blue)

red.switch("hex")

print(red)
print(red.red)
print(red.green)
print(red.blue)

red.switch("hsl")

print(red)
print(red.hue)
print(red.saturation)
print(red.lightness)

try:
    red.switch("this is invalid")
except Exception as e:
    print(e)
try:
    invalid = color.Color("This is not valid")
except Exception as e:
    print(e)
