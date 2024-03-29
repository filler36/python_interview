import time
from concurrent.futures import ThreadPoolExecutor


def calculate(number):
    print(f'Calculating the result for number: {number}')
    time.sleep(4)
    return number ** 2


with ThreadPoolExecutor(max_workers=2) as pool:
    task1 = pool.submit(calculate, 1)
    task2 = pool.submit(calculate, 2)
    task3 = pool.submit(calculate, 3)
    task4 = pool.submit(calculate, 4)
    task5 = pool.submit(calculate, 5)

    print('Hello World')  # Will be printed without waiting for tasks to complete
    print(f'task 1 result: {task1.result()}')  # Will be printed only after task1 will be completed
