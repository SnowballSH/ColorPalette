"""
Constants for print statements in terminal.
Add color to beginning of the statement you want color of.

Example:

print(FontColor.RED + "this is red text")
print(BackgroundColor.MAGENTA + "this has magenta background with red text")
print(FontColor.RESET+"This only has magenta background")
print(RESET_ALL + "normal")
print(TextDecoration.ITALIC + "italicised")
print(RESET_ALL) # Try to RESET EVERYTHING before you exit program. All other programs will use the fonts that was used in your program.
"""

class ColorCode(object):
	def __init__(self, value):
		self.value = f"\033[{value}m"
	
	def __str__(self):
		return str(self.value)

	def __add__(self, other):
		return str(self) + other

	def __radd__(self, other):
		return other + str(self)
	
	def __repr__(self):
		return str(self.value)

class FontColor(object):
	BLACK = ColorCode(30)
	RED = ColorCode(31)
	GREEN = ColorCode(32)
	YELLOW = ColorCode(33)
	BLUE = ColorCode(34)
	MAGENTA = ColorCode(35)
	CYAN = ColorCode(36)
	WHITE = ColorCode(37)
	RESET = ColorCode(39)

class BackgroundColor(object):
	BLACK = ColorCode(40)
	RED = ColorCode(41)
	GREEN = ColorCode(42)
	YELLOW = ColorCode(43)
	BLUE = ColorCode(44)
	MAGENTA = ColorCode(45)
	CYAN = ColorCode(46)
	WHITE = ColorCode(47)
	RESET = ColorCode(49)

class TextDecoration(object):
	NORMAL = ColorCode(22)
	DIM = ColorCode(2)
	BOLD = ColorCode(1)
	BRIGHT = BOLD
	ITALIC = ColorCode(3)
	ITALICS = ITALIC

RESET_ALL = ColorCode(0)
