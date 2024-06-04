"""
The globals() function returns the dictionary implementing the current module namespace.
You even can use it to access the objects in the global namespace.

While globals() can be useful for inspecting and modifying global variables,
it's generally considered best practice to access and modify global variables directly instead of using `globals()`.
Using `globals()` can make code less readable and harder to maintain because it can lead to unexpected side effects and
debugging difficulties. It's typically better to work with global variables in a more controlled and explicit manner.
"""

print(globals())  # Output will show a dictionary containing global variables and their values.
a = 'a is 1'
print(globals()['a'])  # a is 1
a = 'a is 2'
print(globals()['a'])  # a is 2

# Adding a new global variable using globals(). Not recommended.
globals()['b'] = 'b is 3'
print(b)  # Now, b is 3. However Pycharm will highlight b because it thinks that b is not specified

def test():
    print(globals())


test()  # {..., 'test': <function test at 0x000002C7042E85E0>}
