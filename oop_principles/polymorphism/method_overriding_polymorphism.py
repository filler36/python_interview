"""
Run-time polymorphism in Python is typically achieved through method overriding.
You can override methods in a subclass to provide specific implementations.
The method that gets called is determined at runtime based on the object's actual type.
"""


class Animal:
    def make_sound(self):
        print("Animal makes a sound")


class Dog(Animal):
    def make_sound(self):
        print("Dog barks")


my_animal = Dog()
my_animal.make_sound()  # Calls the overridden method in the Dog class

"""
So subtype and ducktype polymorphism looks similar as they both have different classes with the same methods?


Yes, they can look similar at first glance because both involve using methods that have the same name in different classes. However, there are key differences:

Subtype Polymorphism (also known as Inclusion Polymorphism), comes from inheritance where a subclass inherits from a superclass
but overrides the superclass's method. The key point here is that there's a clear parent-child relationship between the classes and it requires an explicit inheritance hierarchy.

On the other hand, Duck Typing does not require an inheritance hierarchy. Two completely unrelated classes can have methods of the same name,
and those methods can be called without regard to the actual class of the object. The only important factor is that the object has a method
with the proper name and it performs the function required at that point in the code.

In other words, Subtype Polymorphism is more about "is-a" relationships (a Dog is an Animal), while Duck Typing is about "behaves-as" relationships
(if it flies like a Bird, it can be treated as a Bird, regardless of what it actually is)."""