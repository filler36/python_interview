"""
If you want to use `from some_package import *` import syntax you should:
1. Import to the __init__ module of the package all necessary names
2. Initialize __all__ tuple attribute with these names which will be imported during `from some_package import *` call

method3 is not added here to the __all__ attribute.
In that case it will not be imported during `from some_package import *` call
"""

from packages.package_example_all.some_package1.module1 import method1
from packages.package_example_all.some_package1.module2 import method2, method3


__all__ = ('method1', 'method2')
