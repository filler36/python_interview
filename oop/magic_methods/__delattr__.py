class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __delattr__(self, item):
        """
        This magic method is automatically executed when you are deleting instance attribute
        We can somehow rewrite default behavior of this method. For example, we can restrict deleting some attributes
        """
        print(f'__delattr__ was called with {item}')
        if item == 'z':
            raise ValueError('Access denied')  # Restrict deleting attribute 'z'
        return object.__delattr__(self, item)


p = Point(1, 2, 3)

# Deleting instance attributes
print(p.__dict__)
del p.x
print(p.__dict__)
delattr(p, 'y')
print(p.__dict__)
del p.z
