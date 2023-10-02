"""
In Python, the `dir()` function is a built-in function that returns a list of all the names
(attributes, methods, and functions) defined in a module, object, or the current scope.
It can be used to inspect the contents of a module, class, or any other Python object.
The `dir()` function does not provide detailed information about these names;
it simply returns their names as strings in a list.

Here's how you can use the `dir()` function:
"""


# 1. To list the attributes and methods of a module:
import math
print(dir(math))  # ['__doc__', '__loader__', '__name__', '__package__', '__spec__', 'acos', 'acosh', 'asin', 'asinh', 'atan', 'atan2', 'atanh', 'ceil', 'comb', 'copysign', 'cos', 'cosh', 'degrees', 'dist', 'e', 'erf', 'erfc', 'exp', 'expm1', 'fabs', 'factorial', 'floor', 'fmod', 'frexp', 'fsum', 'gamma', 'gcd', 'hypot', 'inf', 'isclose', 'isfinite', 'isinf', 'isnan', 'isqrt', 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'log2', 'modf', 'nan', 'perm', 'pi', 'pow', 'prod', 'radians', 'remainder', 'sin', 'sinh', 'sqrt', 'tan', 'tanh', 'tau', 'trunc']

# 2. To list the attributes and methods of an object:
my_list = [1, 2, 3]
print(dir(my_list))  # ['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']

# 3. To list the names in the current scope:
# In this case, it will list the variables and functions defined in the current scope.
print(dir())  # ['__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'math', 'my_list']

"""
Keep in mind that the output of `dir()` can be quite extensive, especially for built-in modules or complex objects.
It includes both the names defined in the object itself and those inherited from its parent classes or modules.
"""
