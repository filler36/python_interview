class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __getattribute__(self, item):
        """
        This magic method is automatically executed when you are accessing instance attribute
        We can somehow rewrite default behavior of this method. For example, we can restrict access to attribute 'y'
        """
        print('__getattribute__ was called')
        return object.__getattribute__(self, item)

    def __getattr__(self, item):
        """
        This magic method is automatically executed after __getattribute__
        when you are accessing NOT EXISTENT instance attribute
        We can somehow rewrite default behavior of this method.
        For example, we can return None for not existent attributes instead of raising default 'AttributeError'
        """
        print('__getattr__ was called')
        return None


p = Point(1, 2)

# Accessing existent instance attributes
print(p.x)
print(p.y)

# Accessing not existent instance attributes
print(p.z)
