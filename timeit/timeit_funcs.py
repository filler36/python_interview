# The timeit module is a built-in library in Python programming
# timeit is used to measure the execution time for the small python code snippets
# This module runs the code a million times (by default) to get the most precise value for the code execution time

import timeit

code_snippet = '''
def square_number():
    for i in range(100000):
        print(i**2)
    print(datetime.datetime.now())

square_number()
'''

# timeit function
print(timeit.timeit(stmt=code_snippet, setup='import datetime', number=1))

# repeat function takes one extra arg 'repeat' and returns output results for multiple code executions
#print(timeit.repeat(stmt=code_snippet, setup='import datetime', number=1, repeat=2))
