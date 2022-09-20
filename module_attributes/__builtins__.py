"""
builtins module provides direct access to all ‘built-in’ identifiers of Python
for example, builtins.print is the full name for the built-in function print()
"""

import builtins
builtins.print('Hello World!')
print(dir(builtins))  # The value of __builtins__ is normally builtins module

print(dir())  # Show the names in the module namespace
print(dir(__builtins__))  # The value of __builtins__ is normally builtins module
