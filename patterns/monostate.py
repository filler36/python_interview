"""
A monostate is a "conceptual singleton" - all data members of a monostate are static, so all instances of the monostate use the same (static) data.
Applications using a monostate can create any number of instances that they desire, as each instance uses the same data.
"""


class MonostateExample:
    __shared_attrs = {
        'name': 'Filip',
        'id': 1
    }

    def __init__(self):
        self.__dict__ = self.__shared_attrs


m1 = MonostateExample()
m2 = MonostateExample()
print(m1.id)  # 1
print(m2.id)  # 1
m1.id = 2
print(m1.id)  # 2
print(m2.id)  # 2
m2.x = 'test'
print(m1.x)  # test
print(m2.x)  # test
