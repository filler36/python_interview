"""
The super() function works with the Method Resolution Order (MRO).

super().some_method(arg) in our example will be called from B class since some_method will first will be found in the B class
If B class did not have some_method A.some_method() would be called
"""


class A:
    def some_method(self, arg):
        print(f'some_method called from A: {arg}')


class B(A):
    def some_method(self, arg):
        print(f'some_method called from B: {arg}')


class C(B):
    def some_method(self, arg):
        super().some_method(arg)  # This does the same thing as:
                                  # super(C, self).method(arg)


c = C()
c.some_method('hello')
