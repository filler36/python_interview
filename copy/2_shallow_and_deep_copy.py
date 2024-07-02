import copy


class Test:
    lst1 = [1, 2, 3]

    def __init__(self):
        self.lst2 = [1, 2, 3]


t1 = Test()
t2 = copy.copy(t1)
t3 = copy.deepcopy(t1)

# lst1 will not be deep copied since it is the class attribute
print(id(t1.lst1))  # The same object
print(id(t2.lst1))  # The same object
print(id(t3.lst1))  # The same object

print()

# lst2 will be deep copied since it is the class attribute
print(id(t1.lst2))  # The same object
print(id(t2.lst2))  # The same object
print(id(t3.lst2))  # Completely new object
