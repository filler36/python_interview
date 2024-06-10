class Point:
    """
    Here we have protected attributes _x, _y and protected method _print_data
    Protected attributes can be accessed from within class and subclassess
    """
    def __init__(self, x, y):
        self._x = x
        self._y = y

    def _print_data(self):
        print(f'Point(x={self._x}, y={self._y})')


p = Point(1, 2)
print(p._x)  # Pycharm will highlight warning "Access to a protected member _x of a class"
p._print_data()  # Pycharm will highlight warning "Access to a protected member _print_data of a class "
