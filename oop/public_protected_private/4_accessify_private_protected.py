from accessify import private, protected


class Point:
    """
    Here we have public attributes x, y and public method print_data
    """
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @protected
    def print_data(self):
        print(f'Point(x={self.x}, y={self.y})')

    @private
    def print_data2(self):
        print(f'Point(x={self.x}, y={self.y})')


p = Point(1, 2)
#p.print_data()  # accessify.errors.InaccessibleDueToItsProtectionLevelException: Point._print_data() is inaccessible due to its protection level
p.print_data2()  # accessify.errors.InaccessibleDueToItsProtectionLevelException: Point.print_data2() is inaccessible due to its protection level
