def int_hex(value) -> str:
    return '{:x}'.format(value).zfill(2)


def hex_int(value) -> int:
    return int(value, 16)


def rgb_hex(value) -> str:
    return "".join(int_hex(c) for c in value)


def hex_rgb(value) -> tuple:
    return tuple(hex_int(c) for c in value)
