class A1:
    x = 'A1'
    pass


class B1:
    x = 'B1'
    pass


class A(A1):
    x = 'A'
    pass


class B(B1):
    x = 'B'
    pass


class C(A, B):
    #x = 'C'
    pass


# Method Resolution Order: C -> A -> A1 -> B -> B1
# The same order for methods
print(C.__mro__)  # (<class '__main__.C'>, <class '__main__.A'>, <class '__main__.A1'>, <class '__main__.B'>, <class '__main__.B1'>, <class 'object'>)
