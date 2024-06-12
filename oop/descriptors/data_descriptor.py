class CoordinateDescriptor:
    @classmethod
    def verify_coordinate(cls, coordinate):
        if not isinstance(coordinate, int):
            raise TypeError('Invalid coordinate type')

    def __set_name__(self, owner, name):
        self.name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        self.verify_coordinate(value)
        setattr(instance, self.name, value)


class Point:
    x = CoordinateDescriptor()
    y = CoordinateDescriptor()
    z = CoordinateDescriptor()

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z


p1 = Point(1, 2, 3)
print(p1.__dict__)
print(p1.x)
p1 = Point('1', 2, 3)  # TypeError: Invalid coordinate type
