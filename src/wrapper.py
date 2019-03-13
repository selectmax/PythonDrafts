def wrapper(function_for_wrapping):
    def inner(*args, **kwargs):
        print("Function Name: {}".format(function_for_wrapping.__name__))
        return function_for_wrapping(*args, **kwargs)
    return inner


wr = wrapper(print)
wr("Hello!")
