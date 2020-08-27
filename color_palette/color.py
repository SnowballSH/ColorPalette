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
        if self.mode == "rgb":
            return self.value[0]
        elif self.mode == "hex":
            return self.value[0:2]

    @property
    def blue(self):
        if self.mode == "rgb":
            return self.value[1]
        elif self.mode == "hex":
            return self.value[2:4]

    @property
    def green(self):
        if self.mode == "rgb":
            return self.value[2]
        elif self.mode == "hex":
            return self.value[4:6]

    @checks.mode_check
    def switch(self, mode: str):
        if mode == "rgb":
            self.value = conversion.hex_rgb(self.value)
            self.mode = mode
        elif mode == "hex":
            self.value = conversion.rgb_hex(self.value)
            self.mode = mode

    def to_rgb(self):
        if self.mode != "rbg":
            self.value = conversion.hex_rgb(self.value)
            self.mode = "rgb"

    def to_hex(self):
        if self.mode != "hex":
            self.value = conversion.rgb_hex(self.value)
            self.mode = "hex"

    def __repr__(self):
        return f"Color {self.value} with mode '{self.mode}'"