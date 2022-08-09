class PowerIterator:
    """ This custom iterator generates numbers in range [0, limit] to the defined power """
    def __init__(self, power=2, limit=5):
        self.number = 0
        self.power = power
        self.limit = limit

    def __iter__(self):
        return self

    def __next__(self):
        if self.number <= self.limit:
            result = self.number ** self.power
            self.number += 1
            return result
        raise StopIteration


i = iter(PowerIterator())

print(next(i))
print(next(i))
print(next(i))
print(next(i))
print(next(i))
# print(next(i))  # This statement will raise exception StopIteration
