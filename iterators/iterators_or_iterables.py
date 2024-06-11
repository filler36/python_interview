"""
Iteration is a general term for taking each item of something, one after another
Any time you use a loop, explicit or implicit, to go over a group of items, that is iteration
"""
for i in range(5):  # This is the process of iteration
    ...

"""
An iterable object is an object that implements __iter__, which is expected to return an iterator object.
So an iterable is an object that you can get an iterator from. For example: String object

An iterator object implements __next__, which is expected to return the next element of the iterable object that returned it,
and to raise a StopIteration exception when no more elements are available.
"""

str1 = 'Hello World!'  # This String is ITERABLE object
str_iter = iter(str1)  # This iter func will call str1.__iter__ internal method and will return ITERATOR object
print(type(str1))  # <class 'str'>
print(type(str_iter))  # <class 'str_iterator'>

# An iterator is an object with a __next__ method
print(next(str_iter))  # This next func will call str_iter.__next__ internal method
print(next(str_iter))
