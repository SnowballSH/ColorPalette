PyColorPalette
====================
Python Package for easy coloring

Requirements
------------
* `Python`_ 3.6.0+

.. _Python: https://python.org/

Installation
------------
It hasn't come out on pypi yet. To install, just install through git

Install with git bash command:

``python -m pip install git+https://github.com/SnowballSH/color_palette.git@master``

Usage
------------

>>> from color_palette import Color
>>> my_rgb = Color((255, 0, 0)) # You can either call on rbg
>>> print(rgb.blue, rbg.red, rgb.green) # You can print the different values with both hex and rgb
>>> my_hex = rgb.switch("hex") # You can switch from rgb to hex using this or the .to_rbg and .to_hex commands

Contribute
------------
Found bugs? Want to suggest something? Create an issue.

Or you can fork this project and create a pull request.

Do these things
`Here`_

.. _Here: https://github.com/SnowballSH/color_palette/

