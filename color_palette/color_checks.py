from functools import wraps
from . import errors, color


def mode_check(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        mode = args[0].mode
        if not mode != args[1]:
            return
        if mode not in color.ALLOWED_MODES:
            return errors.raiseColorModeError(args[1])

        return func(*args, **kwargs)

    return wrapper


def value_check(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        value = args[0].value
        mode = args[0].mode
        if (mode == 'rgb' and len(value) != 3) or (mode == 'hex' and len(value) != 6):
            return errors.raiseColorValueError(args[1])

        return func(*args, **kwargs)

    return wrapper
