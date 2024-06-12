class Person:
    def __init__(self, name):
        self.__name = name

    def set_name(self, name):
        print('set_name called')
        self.__name = name

    def get_name(self):
        print('get_name called')
        return self.__name

    def delete_name(self):
        print('delete_name called')
        self.__name = None

    name = property(get_name, set_name, delete_name)  # Property object


p = Person('Filip')
print(p.__dict__)  # {'_Person__name': 'Filip'}
print(p.name)  # getter called
p.name = 'John'  # setter called
print(p.name)
del p.name  # deleter called
print(p.__dict__)  # {'_Person__age': 33}
