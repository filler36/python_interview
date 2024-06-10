class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __setattr__(self, key, value):
        """
        This magic method is automatically executed when you are setting instance variable
        We can also somehow rewrite the logic of this method. For example, we can restrict to set some attribute names
        We can also check values for correctness
        """
        print(f'__setattr__ was called with {key}={value}')
        if key not in ('x', 'y'):  # Restrict to set attribute names different from 'x' or 'y'
            raise AttributeError('Invalid name of attribute')
        if not isinstance(value, int):  # Accept only integer values
            raise ValueError('Invalid value type')

        # self.key = value  # Incorrect. This will give us 'RecursionError: maximum recursion depth exceeded'
        # self.__dict__[key] = value  # Correct, but not recommended
        object.__setattr__(self, key, value)  # The best native way to set attribute

print('Instantiate Point')
p = Point(1, 2)

print()
p.x = 3
print(p.x)

print()
setattr(p, 'x', 4)  # setattr function will call __setattr
print(p.x)

print()
p.x = '5'  # Raise 'ValueError: Invalid value type'
#p.z = 5  # Raise 'AttributeError: Invalid name of attribute'

