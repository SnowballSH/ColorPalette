from .color import Color
from tkinter import colorchooser


def pick_raw(mode: int = -1):
    """
    Pick any color you want, returned as raw tuple or string
    :param mode: 0 => rgb, 1 => hex, others => all
    :return: tuple or str
    """
    chosen = colorchooser.askcolor(title='Pick a color')
    return chosen[mode] if 0 <= mode < 2 else chosen


def pick():
    """
    Pick any color you want, returned as color_palette.Color
    :return: Color
    """
    chosen = colorchooser.askcolor(title='Pick a color')
    return Color(chosen[0])
