class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @name.deleter
    def name(self):
        del self.__name

p = Person('Filip', 33)
print(p.__dict__)  # {'_Person__name': 'Filip', '_Person__age': 33}
print(p.name)  # getter called
p.name = 'Philip'  # setter called
print(p.name)
del p.name  # deleter called
print(p.__dict__)  # {'_Person__age': 33}
