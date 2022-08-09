class InfinitePowerIterator:
    """ This custom iterator generates numbers in range [0, infinite] to the defined power """
    def __init__(self, power=2):
        self.number = 0
        self.power = power

    def __iter__(self):
        return self

    def __next__(self):
        result = self.number ** self.power
        self.number += 1
        return result

    def __call__(self, *args, **kwargs):
        return self.__next__()


i = iter(InfinitePowerIterator(), 16)  # Second arg here is a Sentinel
print(next(i))
print(next(i))
print(next(i))
print(next(i))
print(next(i))  # StopIteration will raise here because this statement returns 16 that equals Sentinel argument
