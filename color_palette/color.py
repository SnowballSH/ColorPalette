from . import conversion, errors, color_checks

ALLOWED_MODES = ("rgb", "hex", "hsl")

class Color:
    """Color class for all features."""
    def __init__(self, mode=None, value=(0, 0, 0)):
        self.mode = mode
        if self.mode == None:
            if type(self.value) == tuple:
                if type(self.value[1:]) == float: self.mode = 'hsl'
                else: self.mode = 'rgb'
            elif type(self.value) == str:
                self.mode = "hex"

        self.value = value
        if ('#' in self.value) and self.mode == 'hex':
            self.value = self.value.split('#')[1]

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
    
    @property
    def hue(self):
        if self.mode == "hsl":
            return self.value[0]
        else:
            errors.raiseColorModeError()

    @property
    def saturation(self):
        if self.mode == "hsl":
            return self.value[1]
        else:
            errors.raiseColorModeError()

    @property
    def lightness(self):
        if self.mode == "hsl":
            return self.value[2]
        else:
            errors.raiseColorModeError()

    @property
    def hex(self):
        """Returns the hex value"""
        if self.mode == "rgb":
            return conversion.rgb_hex(self.value)
        else:
            pass

    @property
    def rgb(self):
        """Returns the rgb value"""
        if self.mode == "hex":
            return conversion.hex_rgb(self.value)
        else:
            pass

    @property
    def hsl(self):
        """Returns the hsl value"""
        if self.mode == "rgb":
            conversion.rgb_hsl(self.value)
        else:
            conversion.hex_hsl(self.value)

    @color_checks.mode_check
    def switch(self, mode: str):
        """Switches the color to the given mode"""
        if mode == "rgb":
            self.value = conversion.hex_rgb(self.value)
            self.mode = mode
        elif mode == "hex":
            self.value = conversion.rgb_hex(self.value)
            self.mode = mode

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
        return f"{self.__class__.__name__} {self.value} with mode '{self.mode}'"

    def __eq__(self, other):
        if other.mode == self.mode and self.value == other.value:
            return True
        return other.mode != self.mode and other.hex == self.hex


class Colour(Color):
    """Alias to Color"""
    def __init__(self, mode=None, value=(0, 0, 0)):
        super().__init__(mode, value)


def rgb_color(*, red, green, blue):
    """Creates a Color instance of rgb"""
    return Color((red, green, blue))


def hex_color(*, code):
    """Creates a Color instance of hex"""
    return Color(str(code))


def rgb_colour(*, red, green, blue):
    """Creates a Colour instance of rgb"""
    return Colour((red, green, blue))


def hex_colour(*, code):
    """Creates a Colour instance of hex"""
    return Colour(str(code))

test = Colour("hex", '#ffffff')
