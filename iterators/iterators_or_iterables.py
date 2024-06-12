"""
Iteration is a general term for taking each item of something, one after another
Any time you use a loop, explicit or implicit, to go over a group of items, that is iteration
"""
for i in range(5):  # This is the process of iteration
    ...

"""
ITERABLE
An object capable of returning its members one at a time. Examples of iterables include all sequence types
(such as list, str, and tuple) and some non-sequence types like dict, file objects, and objects of any classes
you define with an __iter__() method or with a __getitem__() method that implements sequence semantics.
Iterables can be used in a for loop and in many other places where a sequence is needed (zip(), map(), …).
When an iterable object is passed as an argument to the built-in function iter(), it returns an iterator for the object.
This iterator is good for one pass over the set of values.
When using iterables, it is usually not necessary to call iter() or deal with iterator objects yourself.
The for statement does that automatically for you, creating a temporary unnamed variable to hold the iterator for the duration of the loop
"""

"""
An ITERATOR object implements __next__, which is expected to return the next element of the iterable object that returned it,
and to raise a StopIteration exception when no more elements are available.
"""

str1 = 'Hello World!'  # This String is ITERABLE object
str_iter = iter(str1)  # This iter func will call str1.__iter__ internal method and will return ITERATOR object
print(type(str1))  # <class 'str'>
print(type(str_iter))  # <class 'str_iterator'>

# An iterator is an object with a __next__ method
print(next(str_iter))  # This next func will call str_iter.__next__ internal method
print(next(str_iter))
