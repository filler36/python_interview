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

class Iterable1:
    def __iter__(self):
        return (x for x in range(4))


class Iterable2:
    def __getitem__(self, index):
        if index < 4:
            return index
        raise StopIteration


iterable1 = Iterable1()
for i in iterable1:
    print(i)

print('---')

iterable2 = Iterable2()
for i in iterable2:
    print(i)
