"""
getattr can get class and instance attributes

getattr(some_instance_of_some_class, 'x') - will return 'x' value even if some_instance does not have 'x' attribute, but some_class have this attribute
"""


class Point:
    z = 3

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Point(x={self.x}, y={self.y})'


p = Point(1, 2)
print(getattr(p, 'x'))  # 1
print(getattr(Point, 'z'))  # 3
print(getattr(p, 'z'))  # 3
print(getattr(p, 'q', None))  # None
print(getattr(p, 'q'))  # AttributeError: 'Point' object has no attribute 'q'. You can rewrite this behavior via __getattr__ overriding
