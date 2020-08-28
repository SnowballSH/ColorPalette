# Color Palette

Python Package for easy coloring

# Installation
It hasn't come out on pypi yet. To install, just install through git
```bash
python -m pip install git+https://github.com/SnowballSH/color_palette.git@master
```

## Usage

```py
from color_palette import Color
rgb = Color((255, 0, 0)) # You can either call on rbg
print(rgb.blue, rbg.red, rgb.green) # You can print the different values with both hex and rgb
hex = rgb.switch("hex") # You can switch from rgb to hex using this or the .to_rbg and .to_hex commands
```

# Contribute
Found bugs? Want to suggest something? Create an issue [here](https://github.com/SnowballSH/color_palette/issues).<br>
Or you can fork this project and create a pull request.