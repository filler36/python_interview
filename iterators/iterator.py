class PowerIterator:
    """ This custom iterator generates numbers in range [0, limit] to the defined power """
    def __init__(self, power: int = 2, limit: int = 4):
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


power_iterator = PowerIterator()  # Initialize PowerIterator
i = iter(PowerIterator())  # get iterator object from power_iterator

print(next(i))  # 0
print(next(i))  # 1
print(next(i))  # 4
print(next(i))  # 9
print(next(i))  # 16
# print(next(i))  # This statement will raise exception StopIteration

for i in power_iterator:  # You can use for loop to iterate through iterable object power_iterator
    print(i)
