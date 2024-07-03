"""
The difference is that STORE_FAST is faster (!) than STORE_NAME.
This is because in a function, y is a local but at toplevel it is a global variable.
"""

import dis
import time


def my_func():
    for x in range(20000000):
        y = x ** 2


start = time.perf_counter()
my_func()
end = time.perf_counter()
print(f'execution time in seconds: {end-start}')  # 2.103254200075753

dis.dis(my_func)


print('-----------------')


start = time.perf_counter()
for x in range(20000000):
    y = x ** 2
end = time.perf_counter()
print(f'execution time in seconds: {end-start}')  # 2.664394999970682

dis.dis("""for x in range(20000000):
    y = x ** 2""")
