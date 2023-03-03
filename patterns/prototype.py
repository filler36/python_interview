#The Prototype pattern is a creational design pattern that allows creating new objects by copying existing objects
# without requiring knowledge of their specific classes. In other words, it enables the creation of new objects by cloning existing ones.

# In Python, we can implement the Prototype pattern by defining a prototype object and creating new objects by cloning it.
# Here is an example:

import copy


class Prototype:
    def __init__(self):
        self._objects = {}

    def register_object(self, name, obj):
        self._objects[name] = obj

    def unregister_object(self, name):
        del self._objects[name]

    def clone(self, name, **kwargs):
        obj = copy.deepcopy(self._objects.get(name))
        obj.__dict__.update(kwargs)
        return obj


class MyClass:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"MyClass(name='{self.name}')"


# Create a prototype object
prototype = Prototype()

# Register a new object
my_class = MyClass("original")
prototype.register_object("my_class", my_class)

# Clone the object
new_class = prototype.clone("my_class")
print(new_class)  # MyClass(name='original')

# Clone the object with updated properties
new_class = prototype.clone("my_class", name="updated")
print(new_class)  # MyClass(name='updated')


# In this example, we first define a Prototype class that maintains a dictionary of registered objects.
# The clone method creates a new object by deep copying the registered object with the given name and updating its attributes with the given keyword arguments.

# We then define a MyClass class that we want to create clones of.
# We create an instance of MyClass and register it with the prototype object.
# We then create a new instance of MyClass by cloning the registered object and print it.
# Finally, we create another instance of MyClass with updated attributes by passing additional keyword arguments to the clone method.