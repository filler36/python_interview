import time


def func_logger(debug_level):
    def outer(func):
        def wrapper(*args, **kwargs):
            if debug_level == 'start' or debug_level is None:
                print(f'-- func started at {time.asctime()}')

            func(*args, **kwargs)

            if debug_level == 'end' or debug_level is None:
                print(f'-- func ended at {time.asctime()}')
            print('---------------------------------------------')
        return wrapper
    return outer


@func_logger('start')
def summarize(a, b):
    print(a+b)


@func_logger('end')
def subtract(a, b):
    print(a-b)


@func_logger(None)
def divide(a, b):
    print(a/b)


summarize(2, 2)
subtract(6, 3)
divide(25, 5)
