"""

A1   B1
|    |
A    B
 \  /
  C

Method Resolution Order: C -> A -> A1 -> B -> B1 -> object
"""


class A1:
    pass


class B1:
    pass


class A(A1):
    pass


class B(B1):
    pass


class C(A, B):
    pass


print(C.__mro__)  # (<class '__main__.C'>, <class '__main__.A'>, <class '__main__.A1'>, <class '__main__.B'>, <class '__main__.B1'>, <class 'object'>)
