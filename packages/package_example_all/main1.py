print(globals())

from some_package1 import *

print(globals())

method1()  # method1
method2()  # method2
method3()  # NameError: name 'method3' is not defined.
