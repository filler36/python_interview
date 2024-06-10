"""
delattr can delete class and instance attributes
"""


class Point:
    z = 3

    def __init__(self, x, y):
        self.x = x
        self.y = y


p = Point(1, 2)

delattr(p, 'x')
print(p.__dict__)
delattr(Point, 'z')
