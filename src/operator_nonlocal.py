def cell(value=None):
    def get_func():
        return value

    def set_func(update):
        nonlocal value
        value = update
    return get_func, set_func


get_func, set_func = cell()
set_func(42)
get_func()
