@validate(0, 5)
def set_pixel(pixel_values):
    print("Pixel created!")

def validate(low_bound = 0, upper_bound = 256):
    def real_decorator(func):
        def wrapper(*args):
            pixel = args[0]
            if (pixel[0:2] < upper_bound and pixel[0:2] < low_bound):
                res = func(*args)
            else:
                print("Function call is not valid")
                res = None
            return res
        return wrapper
    return real_decorator
