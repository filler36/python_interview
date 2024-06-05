print(globals())

from some_package2 import *

print(globals())

method1()  # NameError: name 'method1' is not defined.
method2()  # NameError: name 'method2' is not defined.
method3()  # NameError: name 'method3' is not defined.
