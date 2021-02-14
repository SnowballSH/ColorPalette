---

## This project is no longer in active development. It is now read-only!

---

# Color Palette
[![PyPI version](https://badge.fury.io/py/color-palette.svg)](https://pypi.python.org/pypi/color-palette/)
[![PyPI pyversions](https://img.shields.io/pypi/pyversions/color-palette.svg)](https://pypi.python.org/pypi/color-palette/) <!-- will work when setup.py gets pushed to pypi.org -->
![MIT LICENSE](https://img.shields.io/github/license/SnowballSH/ColorPalette)
![Stars](https://img.shields.io/github/stars/SnowballSH/ColorPalette)
![Issues](https://img.shields.io/github/issues/SnowballSH/ColorPalette)
![Forks](https://img.shields.io/github/forks/SnowballSH/ColorPalette)


Python Package for easy coloring

# Installation
github:
```bash
python -m pip install git+https://github.com/SnowballSH/color_palette.git@master
```
Pip:
```bash
pip install color-palette
```

## Usage

```py
from color_palette import Color, mix, presets
my_rgb = Color((255, 0, 0))  # You can either call on rbg
print(my_rgb)  # You can print the different values with both hex and rgb
my_hex = rgb.switch("hex")  # You can switch from rgb to hex using this or the .to_rbg and .to_hex commands
cyan = presets.cyan  # get preset colors to code quicker
mixed = mix([my_rgb, cyan])  # You can even mix them together!
yellow = presets.yellow[1.6]  # You can get shades and tints for colors by using [amount] after color -- 0 is the original color
print(yellow)  # In this case, 'yellow' is a light yellow color with 1.6 times lighter than normal.
```

# Contribute
Found bugs? Want to suggest something? Create an issue [here](https://github.com/SnowballSH/color_palette/issues).<br>
Or you can fork this project and create a pull request.
