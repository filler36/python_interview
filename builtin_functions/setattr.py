"""
setattr can set class and instance attributes
"""

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Point(x={self.x}, y={self.y})'

p = Point(1, 2)
print(p)  # Point(x=1, y=2)

# Set instance attribute
setattr(p, 'x', 100)
print(p)  # Point(x=100, y=2)

# Set class attribute
setattr(Point, 'z', 3)
print(Point.z)  # 3
print(Point.__dict__)  # {..., 'z': 3}}
