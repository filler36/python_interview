class Point:
    """
    Here we have public attributes x, y and public method print_data
    """
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def print_data(self):
        print(f'Point(x={self.x}, y={self.y})')


p = Point(1, 2)
print(p.x)
p.print_data()
