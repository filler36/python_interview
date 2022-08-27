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
print(p.__dict__)
print(p.name)  # getter
p.name = 'Philip'  # setter
print(p.name)
del p.name
print(p.__dict__)
