class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __getattribute__(self, item):
        """
        This magic method is automatically executed when you are accessing instance attribute
        We can somehow rewrite default behavior of this method. For example, we can restrict access to attribute 'y'
        """
        print(f'__getattribute__ was called with {item}')
        return object.__getattribute__(self, item)

    def __getattr__(self, item):
        """
        This magic method is automatically executed after __getattribute__
        when you are accessing NOT EXISTENT instance attribute
        We can somehow rewrite default behavior of this method.
        For example, we can return None for not existent attributes instead of raising default 'AttributeError'
        """
        print(f'__getattr__ was called with {item}')
        return None


p = Point(1, 2, 3)

# Accessing existent instance attributes
print(p.x)  # 1
print(p.y)  # 2
print(getattr(p, 'z'))  # 3. This will also call __getattribute__

# Accessing not existent instance attributes
print(p.q)  # None
