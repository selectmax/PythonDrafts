import time


def timer(func):
    def wrapper(*args, **kwargs):
        starttime = time.time()
        res = func(*args, **kwargs)
        finishtime = time.time()
        print("Starttime = {}, Finishtime = {}\n".format(starttime, finishtime))
        print("Total time: {}".format(finishtime - starttime))
        return res
    return wrapper


@timer
def factorial(number):
    res = 1
    for i in range(1, number):
        res = res * i
    return res


print(factorial(100000))