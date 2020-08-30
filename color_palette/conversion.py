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
    return tuple(hex_int(c) for c in value)


def rgb_hsl(value: tuple) -> tuple:
    """Converts from rgb to hsl"""
    r, g, b = r/255, g/255, b/255
    cmax = max(r, g, b)
    cmin = min(r, g, b)
    diff = cmax - cmin

    hue = None
    if diff == 0: hue = 0
    elif cmax == r: hue = 60 * (((g-b) / diff) % 6)
    elif cmax == g: hue = 60 * (((b-r) / diff) + 2)
    elif cmax == b: hue = 60 * (((r-g) / diff) + 4)

    lightness = (cmax + cmin) / 2

    if diff == 0:
        saturation = 0
    else:
        saturation = diff / (1 - abs (2 * lightness-1))

    return hue, saturation, lightness

def hex_hsl(value: str) -> tuple:
    """Converts from hex to hsl"""
    hex_rgb(value)
    return rgb_hsl((r, g, b))


def hsl_hex(value: tuple) -> str:
    """Converts from hsl to hex"""
    pass

def hsl_rgb(value: tuple) -> tuple:
    """Converts from hsl to rgb"""
    pass
