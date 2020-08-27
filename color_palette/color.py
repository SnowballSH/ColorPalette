from . import conversion, errors

class Color:
    def __init__(self, value=(0, 0, 0)):
        self.mode = "rgb" if type(value) in [list, tuple] else "hex" if type(value) == str else None
        if self.mode is None or (self.mode == 'rgb' and len(value) != 3) or (self.mode == 'hex' and len(value) != 6):
            errors.raiseColorValueError(value)
        self.value = value
        self.red = None
        self.green = None
        self.blue = None

        if self.mode == "rgb":
            self.red = self.value[0]
            self.green = self.value[1]
            self.blue = self.value[2]

        elif self.mode == "hex":
            self.red = self.value[0:2]
            self.green = self.value[2:4]
            self.blue = self.value[4:6]

        else:
            errors.raiseColorModeError(self.mode)

    def switch(self, mode: str):
        if mode != self.mode:
            if mode == "rgb":
                self.value = conversion.hex_rgb(self.value)
                self.red = self.value[0]
                self.green = self.value[1]
                self.blue = self.value[2]
                self.mode = mode

            elif mode == "hex":
                self.value = conversion.rgb_hex(self.value)
                self.red = self.value[0:2]
                self.green = self.value[2:4]
                self.blue = self.value[4:6]
                self.mode = mode

            else:
                errors.raiseColorModeError(mode)

    def __repr__(self):
        return f"Color {self.value} with mode '{self.mode}'"
