from . import conversion, errors, color_checks

ALLOWED_MODES = ("rgb", "hex")


class Color:
    """Color class for all features."""

    def __init__(self, value=(0, 0, 0), mode=None):
        self.mode = mode
        self.value = value

        if self.mode is None:
            if type(self.value) == tuple and len(self.value) == 3:
                self.mode = 'rgb'
            elif type(self.value) == str and len(self.value) == 6:
                self.mode = "hex"
            else:
                errors.raiseColorValueError(self.value)

        if ('#' in self.value) and self.mode == 'hex':
            self.value = self.value.split('#')[1]

        if self.mode not in ALLOWED_MODES:
            errors.raiseColorModeError(self.mode)

    def red(self):
        """Returns the red value of the color."""
        if self.mode == "rgb":
            return self.value[0]
        elif self.mode == "hex":
            return self.value[0:2]
        else:
            errors.raiseColorModeError()

    def green(self):
        """Returns the green value of the color."""
        if self.mode == "rgb":
            return self.value[1]
        elif self.mode == "hex":
            return self.value[2:4]
        else:
            errors.raiseColorModeError()

    def blue(self):
        """Returns the blue value of the color."""
        if self.mode == "rgb":
            return self.value[2]
        elif self.mode == "hex":
            return self.value[4:6]
        else:
            errors.raiseColorModeError()

    def hex(self):
        """Returns the hex value"""
        return conversion.rgb_hex(self.value)

    def rgb(self):
        """Returns the rgb value"""
        return conversion.hex_rgb(self.value)

    @color_checks.mode_check
    def switch(self, mode: str):
        """Switches the color to the given mode"""
        if mode == "rgb":
            self.value = conversion.hex_rgb(self.value)
            self.mode = mode
        elif mode == "hex":
            self.value = conversion.rgb_hex(self.value)
            self.mode = mode
        else:
            errors.raiseColorModeError(mode)

    def to_rgb(self):
        """Changes color to rgb"""
        if self.mode != "rgb":
            self.value = conversion.hex_rgb(self.value)
            self.mode = "rgb"
        return self

    def to_hex(self):
        """Changes color to hex"""
        if self.mode != "hex":
            self.value = conversion.rgb_hex(self.value)
            self.mode = "hex"
        return self

    def __repr__(self):
        return str(self.value)

    def __eq__(self, other):
        if other.mode == self.mode and self.value == other.value:
            return True
        return other.mode != self.mode and other.hex == self.hex


def rgb_color(rgb):
    """Creates a Color instance of rgb"""
    return Color(rgb)


def hex_color(code):
    """Creates a Color instance of hex"""
    return Color(str(code))


# ALIAS

Colour: classmethod = Color

rgb_colour = rgb_color
hex_colour = hex_color
