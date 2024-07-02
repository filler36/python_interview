"""
Abstraction is a fundamental concept in Object-Oriented Programming (OOP) that allows us to model complex systems in a simplified and organized manner.
It involves focusing on the essential features of an object or system while hiding irrelevant details.
We can create more manageable and reusable code by abstracting unnecessary complexity.

Abstraction    Focus - Hiding unnecessary details and providing simplification
Encapsulation  Focus - Bundling data and methods together within a class

In OOP, abstraction involves creating abstract classes or interfaces that define a blueprint for other classes to inherit from.
These abstract entities cannot be instantiated directly but serve as a foundation for creating concrete classes that implement their methods and properties.

The main goal of abstraction is to provide a simplified and well-defined interface for interacting with objects,
shielding the user from unnecessary complexity. It allows programmers to focus on high-level concepts and modularize code,
enhancing maintainability, reusability, and overall code quality.
"""
from abc import ABC, abstractmethod


class CarDrivingInterface(ABC):
    """
    This interface is an abstraction.
    By exposing these methods we abstracted from a concrete implementation realization.
    We just show what methods should be used by user who will use this interface.
    Concrete implementation/realization is not important to the user. It should only use these methods to drive car.
    """
    @abstractmethod
    def start_engine(self):
        pass

    @abstractmethod
    def stop_engine(self):
        pass

    @abstractmethod
    def drive(self):
        pass

    @abstractmethod
    def brake(self):
        pass


class SkodaFabia(CarDrivingInterface):
    def start_engine(self):
        print('---')
        print('Push clutch pedal')
        print('Turn ignition key')
        print('Skoda Fabia engine started')

    def stop_engine(self):
        print('---')
        print('Turn ignition key')
        print('Skoda Fabia engine stopped')

    def drive(self):
        print('---')
        print('Skoda Fabia is driving')

    def brake(self):
        print('---')
        print('Skoda Fabia is braking')

f1 = SkodaFabia()
f1.start_engine()
f1.drive()
f1.brake()
f1.stop_engine()

