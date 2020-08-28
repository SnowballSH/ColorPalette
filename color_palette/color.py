from . import conversion, errors, checks

ALLOWED_MODES = ("rgb", "hex")

class Color:
    def __init__(self, value=(0, 0, 0)):
        self.mode = "rgb" if type(value) in [list, tuple] else "hex" if type(value) == str else None
        if self.mode is None or (self.mode == 'rgb' and len(value) != 3) or (self.mode == 'hex' and len(value) != 6):
            errors.raiseColorValueError(value)
        self.value = value

        if not self.mode in ALLOWED_MODES:
            errors.raiseColorModeError(self.mode)

    @property
    def red(self):
        """Returns the red value of the color."""
        if self.mode == "rgb":
            return self.value[0]
        elif self.mode == "hex":
            return self.value[0:2]

    @property
    def blue(self):
        """Returns the blue value of the color."""
        if self.mode == "rgb":
            return self.value[1]
        elif self.mode == "hex":
            return self.value[2:4]

    @property
    def green(self):
        """Returns the green value of the color."""
        if self.mode == "rgb":
            return self.value[2]
        elif self.mode == "hex":
            return self.value[4:6]

    @checks.mode_check
    def switch(self, mode: str):
        """Switches the color to the given mode"""
        if mode == "rgb":
            self.value = conversion.hex_rgb(self.value)
            self.mode = mode
        elif mode == "hex":
            self.value = conversion.rgb_hex(self.value)
            self.mode = mode

    def to_rgb(self):
        """Returns a new instance of hex color"""
        if self.mode != "rbg":
            value = conversion.hex_rgb(self.value)
            return rgb_color(red=value[0], green=value[1], blue=value[2])
        return self

    def to_hex(self):
        """Returns a new instance of hex color"""
        if self.mode != "hex":
            value = conversion.rgb_hex(self.value)
            return hex_color(code=value)
        return self

    def __repr__(self):
        return f"Color {self.value} with mode '{self.mode}'"

    def __eq__(self, other):
        if other.mode == self.mode and self.value == other.value:
            return True
        return other.mode != self.mode and other.to_hex() == self.to_hex()


def rgb_color(*, red, green, blue):
    return Color((red, green, blue))


def hex_color(*, code):
    return Color(str(code))