class A1:
    x = 'A1'
    pass


class A(A1):
    x = 'A'
    pass


class B(A1):
    x = 'B'
    pass


class C(A, B):
    #x = 'C'
    pass


# Method Resolution Order (diamond problem): C -> A -> B -> A1
# Class A and B both inherited from A1 class. In that case A1 moves to the right
# In Python 2 old style classes it was: C -> A -> A1 -> B -> A1
# The same order resolution for methods
print(C.__mro__)  # (<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class '__main__.A1'>, <class 'object'>)

