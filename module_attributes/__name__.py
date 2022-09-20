"""
The __name__ attribute returns the name of the module.
By default, the name of the file (excluding the extension .py) is the value of __name__ attribute.
You can rewrite __name__ attribute in your module_attributes
"""
print(dir())  # Show the names in the module namespace

import math
print(math.__name__)

# When we run any Python script, its __name__ attribute is automatically set to __main__
print(__name__)
