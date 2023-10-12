"""
In Python, the `globals()` function is a built-in function that returns a dictionary representing the current global symbol table.
The global symbol table is a dictionary that contains information about all the global variables and their values in the current scope or module.
When you use the `globals()` function, it provides a way to access and manipulate global variables and their values.
Here's how the `globals()` function works:
"""


"""
When you call `globals()`, it returns a dictionary where the keys are variable names, and the values are the corresponding values of those variables in the current global scope.
You can use this dictionary to inspect or modify global variables. For example:
"""

global_variables = globals()
print(global_variables)  # Output will show a dictionary containing global variables and their values.

x = 10
y = 20

print(global_variables)  # x and y will be added to the globals dict


# Modifying a global variable using globals(). Not recommended.
global_variables['x'] = 30
print(x)  # Now, x is 30

# Adding a new global variable using globals(). Not recommended.
global_variables['z'] = 40
print(z)  # Now, z is 40. However Pycharm will highlight z because it thinks that z is not specified

"""
While globals() can be useful for inspecting and modifying global variables,
it's generally considered best practice to access and modify global variables directly instead of using `globals()`.
Using `globals()` can make code less readable and harder to maintain because it can lead to unexpected side effects and
debugging difficulties. It's typically better to work with global variables in a more controlled and explicit manner.
"""
