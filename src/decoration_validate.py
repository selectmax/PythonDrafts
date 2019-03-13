import functools


def decorator_witharguments(arg):
    def validate(func):
        def wrapper(arg, *args, **kwargs):
            if (low_bound < arg):
                res = func(arg, *args, **kwargs)
            else:
                print("Function call is not valid")
                return None
            return res
        return wrapper
    return validate

@validate(low_bound = 0)
def set_pixel(pixel_values):
    print("Pixel created!")