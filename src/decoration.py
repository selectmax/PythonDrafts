from functools import wraps


def trace(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Вызвана функция: {}".format(func.__name__))
        return func(*args, **kwargs)
    return wrapper

@trace
def useful():
    """Useful function
    """
    print("This is useful function!")


print(useful.__name__)
print(useful.__doc__)