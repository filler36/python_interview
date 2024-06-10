class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __del__(self):
        """
        This method is automatically executed before instance deletion
        """
        print(f'__del__ method was called for instance  {str(self)}')


p = Point(1, 2)
print(p.y)
del p
print(p.y)  # NameError: name 'p' is not defined
