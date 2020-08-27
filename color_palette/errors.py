class ColorModeError(Exception):
    pass


class ColorValueError(Exception):
    pass


def raiseColorModeError(got="", message=None):
    if message is None:
        message = f"Expected mode in ('rgb', 'hex'), got '{got}'"
    raise ColorModeError(message)


def raiseColorValueError(got="", message=None):
    if message is None:
        message = f"Value not in wanted types: '{got}'"
    raise ColorValueError(message)
