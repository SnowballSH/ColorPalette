from . import color, errors


def int_hex(value) -> str:
    """Converts from int to hex"""
    return '{:x}'.format(value).zfill(2)


def hex_int(value) -> int:
    """Converts from hex to int"""
    return int(value, 16)


def rgb_hex(value) -> str:
    """Converts from rbg to hex"""
    return "".join(int_hex(c) for c in value)


def hex_rgb(value) -> tuple:
    """Converts from hex to rbg"""
    return tuple(hex_int(c) for c in [value[:2], value[2:4], value[4:6]])


def convert(target, destination: str = "rgb"):
    if type(target) != color.Color:
        raise errors.ColorValueError(f"'target' parameter must be type Color, not {type(target)}")

    if type(destination) != str:
        errors.raiseColorModeError(destination)

    if target.mode == destination:
        return target

    if target.mode == "rgb":
        return color.Color(rgb_hex(target.value))

    if target.mode == "hex":
        return color.Color(hex_rgb(target.value))
