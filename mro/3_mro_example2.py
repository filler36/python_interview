"""

A    B
 \ / |
  C  |
   \ |
    D

Method Resolution Order: D -> C -> A -> B -> object
"""


class A:
    pass


class B:
    pass


class C(A, B):
    pass


class D(C, B):
    pass


print(D.__mro__)  # (<class '__main__.D'>, <class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>)

