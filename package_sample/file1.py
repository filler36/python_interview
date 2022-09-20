__all__ = ['a', 'hello']  # Will be imported in case of 'from file1 import *'

a = 10
b = 20  # Will not be imported in case of 'from file1 import *'
c = 5.4  # Will not be imported in case of 'from file1 import *'

def hello():
    pass
