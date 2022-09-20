"""
__file__ is an optional attribute which holds the name and path of the module file from which it is loaded
"""
print(dir())  # Show the names in the module namespace
print(__file__)

import io
print(io.__file__)

import math
try:
    print(math.__file__)
except Exception as ex:
    print(ex)