"""
A mixin in Python is a class that contains methods for use by other classes without having to be the parent class of those other classes.
They're a type of multiple inheritance and are used to "mix-in" extra properties or methods into a class.
This can be particularly useful when you want to provide a lot of optional functionality for a class.
"""


class TelMixin:
    def telfunc(self):
        print("I can make calls")


class CameraMixin:
    def camerafunc(self):
        print("I can make photos")


class Phone(TelMixin, CameraMixin):
    def __init__(self, model):
        self.model = model

    def welcome(self):
        print("Welcome {}".format(self.model))


p = Phone('Samsung Galaxy S20')
p.telfunc()
p.camerafunc()
p.welcome()
