"""
Encapsulation is one of the fundamental concepts in object-oriented programming (OOP).
It describes the idea of wrapping data and the methods that work on data within one unit.
This puts restrictions on accessing variables and methods directly and can prevent the accidental modification of data.
To prevent accidental change, an object’s variable can only be changed by an object’s method.
Those types of variables are known as private variables.

A class is an example of encapsulation as it encapsulates all the data that is member functions, variables, etc.
The goal of information hiding is to ensure that an object’s state is always valid by controlling access to attributes that are hidden from the outside world.
"""


class Person:  # Here is example of encapsulation - Class
    def __init__(self, age):
        self.age = age  # We encapsulated data (age) into a Class

    @property
    def age(self):
        return self.__age

    @age.setter  # We use setter to restrict direct access to the data
    def age(self, age):
        if age < 0:
            raise ValueError('Incorrect age!')
        self.__age = age

    def say_hello(self):  # We encapsulated code (method) that works with the data (age) into a Class
        return f'Hello, I am {self.age} years old'


p = Person(10)
print(p.__dict__)  # {'_Person__age': 10}
p.age = -1  # ValueError: Incorrect age!
