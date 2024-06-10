"""
The __dict__ in Python represents a dictionary or any mapping object that is used to store the attributes of the object.
They are also known as mappingproxy objects.
"""


class Point:
    z = 3

    def __init__(self, x, y):
        self.x = x
        self.y = y


p = Point(1, 2)
print(p.__dict__)  # {'x': 1, 'y': 2}
print(Point.__dict__)  # {'__module__': '__main__', 'z': 3, '__init__': <function Point.__init__ at 0x0000027D6C5F8540>, '__dict__': <attribute '__dict__' of 'Point' objects>, '__weakref__': <attribute '__weakref__' of 'Point' objects>, '__doc__': None}
