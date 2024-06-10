class Point:
    """
    Here we have private attributes __x, __y and private method __print_data
    Protected attributes can be accessed only from within class
    """
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def __print_data(self):
        print(f'Point(x={self.__x}, y={self.__y})')


p = Point(1, 2)

# You can overcome that limitation with such syntax
print(p._Point__x)  # 1
p._Point__print_data()  # Point(x=1, y=2)


# If you try to access these attributes in a regular way you will get AttributeError
print(p.__x)  # AttributeError: 'Point' object has no attribute '__x'
p.__print_data()  # AttributeError: 'Point' object has no attribute '__print_data'
