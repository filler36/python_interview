"""
This type of polymorphism is generally called "Duck Typing" (a concept in Python and other dynamic languages),which
allows you to use any object that provides the required behavior without forcing it to inherit from the same parent class.

"Duck Typing" comes from the saying: "If it looks like a duck, swims like a duck, and quacks like a duck,
then it probably is a duck." In the context of programming, it means: If it provides the required method(s)/behavior(s), you can use it.

In your example, both the Sparrow (which is a subclass of Bird) and Airplane classes have a method called "fly".
The "perform_flight" function doesn't care what kind of object it receives, as long as the object can "fly" (i.e., it has a "fly" method), thus demonstrating polymorphism.
"""


class Bird:
    def fly(self):
        pass


class Sparrow(Bird):
    def fly(self):
        print("Sparrow flies")


class Airplane:
    def fly(self):
        print("Airplane flies")


def perform_flight(flying_object):
    flying_object.fly()


sparrow = Sparrow()
airplane = Airplane()

perform_flight(sparrow)  # Output: Sparrow flies
perform_flight(airplane)  # Output: Airplane flies
