from warnings import warn


class ColorModeError(Exception):
    pass


class ColorValueError(Exception):
    pass


class ModeWarning(UserWarning):
    pass


def raiseColorModeError(got="", message=None):
    if message is None:
        message = f"Expected mode in ('rgb', 'hex'), got '{got}'"
    raise ColorModeError(message)


def raiseColorValueError(got="", message=None):
    if message is None:
        message = f"Value not in wanted types: '{got}'"
    raise ColorValueError(message)


def raiseModeWarning(got="", message=None):
    if message is None:
        message = f"""
Got tuple for value, however mode is not given. Our prediction of the mode is {got}
It may be incorrect.
This will cause the program to not work the way you want.
Please specify whether the mode is 'rgb' or 'hsl'.
"""

    warn(message, ModeWarning)
