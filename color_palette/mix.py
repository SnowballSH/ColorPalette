from . import color, conversion
import statistics as st


def mix(colors: list, result: str = "rgb"):
    rgb_colors = list(map(conversion.convert, colors))
    new_r = st.mean(map(color.Color.red, rgb_colors))
    new_g = st.mean(map(color.Color.green, rgb_colors))
    new_b = st.mean(map(color.Color.blue, rgb_colors))
    return conversion.convert(color.Color((new_r, new_g, new_b)), result)
