class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __getattribute__(self, item):
        """
        This magic method is automatically executed when you are accessing instance variable
        We can somehow rewrite default behavior of this method. For example, we can restrict access to attribute 'y'
        """
        print('__getattribute__ was called')
        if item == 'y':
            raise ValueError('Access denied')  # Restrict access to attribute 'y'
        return object.__getattribute__(self, item)


p = Point(1, 2)

# Accessing instance attributes
print(p.x)
print(p.y)
