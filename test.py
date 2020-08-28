from color_palette import color

red = color.Color((255, 20, 30))
print(red)
print(red.red)
print(red.green)
print(red.blue)
red.switch("hex")
print(red)
print(red.red)
print(red.green)
print(red.blue)
red.to_rgb()
try:
    red.switch("this is invalid")
except Exception as e:
    print(e)
try:
    invalid = color.Color("This is not valid")
except Exception as e:
    print(e)

rgb = color.rgb_color(red=10, green=102, blue=24)
print(rgb)
# print(str(rgb))
# hex = rgb.to_hex()
# print(hex)
# print(str(hex))