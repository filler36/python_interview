"""
In Python, __call__ is a special method that enables an instance of a class to be called as a function.
When an object is called as a function, the __call__ method is automatically invoked, and it allows the object to perform some custom action as if it was a function.
"""
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __call__(self, years):
        return f"{self.name} will be {self.age + years} years old in {years} years."


person = Person("John", 30)
print(person(5))  # Output: John will be 35 years old in 5 years.

"""
In the example above, the Person class has a __call__ method that takes in a number of years as an argument and returns a message about the person's age in that many years.
When we call the person object as a function with an argument of 5, the __call__ method is invoked, and it returns the message with the updated age.
The __call__ method can be useful when we want to define an object that behaves like a function and has some additional state or behavior.
By defining the __call__ method, we can make an object callable and give it the ability to execute some custom logic when it's called.
"""
