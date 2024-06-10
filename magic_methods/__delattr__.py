class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __delattr__(self, item):
        """
        This magic method is automatically executed when you are deleting instance attribute
        We can somehow rewrite default behavior of this method. For example, we can restrict deleting some attributes
        """
        print('__delattr__ was called')
        if item == 'y':
            raise ValueError('Access denied')  # Restrict deleting attribute 'y'
        return object.__delattr__(self, item)


p = Point(1, 2)

# Deleting instance attributes
print(p.__dict__)
del p.x
print(p.__dict__)
del p.y
