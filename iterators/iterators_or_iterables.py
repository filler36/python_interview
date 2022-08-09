# Iteration is a general term for taking each item of something, one after another
# Any time you use a loop, explicit or implicit, to go over a group of items, that is iteration
for i in range(5):  # This is the process of iteration
    ...

# An iterable is an object that has an __iter__ method which returns an iterator,
# or which defines a __getitem__ method that can take sequential indexes starting from zero
# (and raises an IndexError when the indexes are no longer valid)
# So an iterable is an object that you can get an iterator from. For example: String object

str1 = 'Hello World!'  # This String is ITERABLE object
str_iter = iter(str1)  # This iter func will call str1.__iter__ internal method and will return ITERATOR object
print(type(str1))  # <class 'str'>
print(type(str_iter))  # <class 'str_iterator'>

# An iterator is an object with a __next__ method
print(next(str_iter))  # This next func will call str_iter.__next__ internal method
print(next(str_iter))