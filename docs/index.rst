.. Color Palette documentation master file, created by
   sphinx-quickstart on Thu Aug 27 19:39:55 2020.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to Color Palette's documentation!
=========================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:



It's simple!

   from color_palette import Color

   rgb = Color((255, 0, 0)) # You can either call on rbg

   print(rgb.blue, rbg.red, rgb.green) # You can print the different values with both hex and rgb

   hex = rgb.switch("hex") # You can switch from rgb to hex using this or the .to_rbg and .to_hex commands



Features
--------

- Python Package for easy coloring

Installation
------------

Install Color Palette by running:

   pip install color_palette

Contribute
----------

- Issue Tracker: https://github.com/SnowballSH/color_palette/issues
- Source Code: https://github.com/SnowballSH/color_palette

Support
-------

If you are having issues, please let us know.