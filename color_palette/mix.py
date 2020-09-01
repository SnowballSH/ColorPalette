from . import color, conversion, errors
import statistics as st


def mix(colors: list, result: str = "rgb"):
    rgb_colors = list(map(conversion.convert, colors))
    new_r = st.mean(map(color.Color.red, rgb_colors))
    new_g = st.mean(map(color.Color.green, rgb_colors))
    new_b = st.mean(map(color.Color.blue, rgb_colors))
    return conversion.convert(color.Color((new_r, new_g, new_b)), result)


def brightness(target, amount):
    if type(target) != color.Color:
        raise errors.ColorValueError(f"'target' parameter must be type Color, not {type(target)}")

    if type(amount) not in (int, float):
        raise ValueError(f"'amount' parameter must be a number, got {type(amount)}")

    new = tuple((m + amount * 255) if m + amount * 255 <= 255 else 255 for m in target.value)
    return color.Color(new)
