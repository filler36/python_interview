"""
If the main script will be started as usual there will be raised AssertionError
If the script will be started as `python -O main.py`, where O stands for optimized,
the assert operator will be ignored and script will finish without any errors.

.pyo: This was a file format used before Python 3.5 for *.pyc files that were created with optimizations (-O)
"""

print('before')

a = 1
b = '1'

assert a == b

print('after')
