PyColorPalette
====================
Python Package for easy coloring

Requirements
------------
* `Python`_ 3.6.0+

.. _Python: https://python.org/

Installation
------------
Install with git bash command:

``python -m pip install git+https://github.com/SnowballSH/color_palette.git@master``

pip:

``pip install color-palette==0.2.4.1``

Usage
------------

>>> from color_palette import Color, mix, presets
>>> my_rgb = Color((255, 0, 0))  # You can either call on rbg
>>> print(my_rgb)  # You can print the different values with both hex and rgb
>>> my_hex = rgb.switch("hex")  # You can switch from rgb to hex using this or the .to_rbg and .to_hex commands
>>> cyan = presets.cyan  # get preset colors to code quicker
>>> mixed = mix.mix([my_rgb, cyan])  # You can even mix them together!
>>> yellow = presets.yellow[1.6]  # You can get shades and tints for colors by using [amount] after color -- 0 is the original color
>>> print(yellow)  # In this case, 'yellow' is a light yellow color with 1.6 times lighter than normal.

Contribute
------------
Found bugs? Want to suggest something? Create an issue.

Or you can fork this project and create a pull request.

Do these things
`Here`_

.. _Here: https://github.com/SnowballSH/color_palette/

