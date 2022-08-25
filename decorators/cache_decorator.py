import random


def cache(func):
    cache_dict = {}

    def wrapper(arg):
        if arg in cache_dict:
            return f'from cache: {cache_dict[arg]}'
        cache_dict[arg] = func(arg)
        return cache_dict[arg]
    return wrapper


@cache
def square_number(x):
    return x**2


randomlist = [random.randint(0, 10) for _ in range(10)]

for i in randomlist:
    print(square_number(i))
