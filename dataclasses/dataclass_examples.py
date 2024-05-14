from dataclasses import dataclass

"""
frozen: When True, the values inside the instance of the class can't be modified after it's created. The default is False.
"""
@dataclass(frozen=True)
class DataClassBook:
    title: str
    author: str
    year: int = 2000

    def test(self):
        print('test')

b1 = DataClassBook('The end', 'Crazy Bob')
b2 = DataClassBook('The end', 'Crazy Bob')

"""
In this case, the comparison is valid because the dataclass creates behind the scenes an __eq__ method, which performs the comparison.
Without the decorator, we'd have to create this method ourselves.
"""
print(id(b1), id(b2))  # IDs will be different
print(b1 == b2)  # True

"""
dataclass implements not only the __init__ method, but several others, including the __repr__ method.
In a regular class,we use this method to display a representation of an object in the class.
"""
print(b1)  # DataClassBook('The end', 'Crazy Bob')
print(b1.__repr__())  # DataClassBook('The end', 'Crazy Bob')
print(b1.__str__())  # DataClassBook('The end', 'Crazy Bob')

b1.year = 1999  # dataclasses.FrozenInstanceError: cannot assign to field 'year'
