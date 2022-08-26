class Point:
    def __new__(cls, *args, **kwargs):
        """
        This method is automatically executed after the class is called
        By default this method is inherited from default 'object' class
        Returns reference to the new instance of the class
        """
        print(f'__new__ method was called from class {str(cls)}')
        return super().__new__(cls)

    def __init__(self, x, y):
        """
        This method is automatically executed after __new__ method
        """
        print(f'__init__ method was called for instance  {str(self)}')
        self.x = x
        self.y = y

p = Point(1,2)
