"""
hasattr can determine if the attribute exist. Can work with classes and instances.

hasattr(some_instance_of_some_class, 'x') - will return True even if some_instance does not have 'x' attribute, but some_class have this attribute
"""


class Point:
    z = 3

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Point(x={self.x}, y={self.y})'


p = Point(1, 2)
print(hasattr(p, 'x'))  # True
print(hasattr(p, 'z'))  # True
print(hasattr(Point, 'z'))  # True
print(hasattr(Point, 'q'))  # False
