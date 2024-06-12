"""
Construct an iterator from those elements of iterable for which function is true.
iterable may be either a sequence, a container which supports iteration, or an iterator.
If function is None, the identity function is assumed, that is, all elements of iterable that are false are removed.
"""
lst1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
f = filter(lambda x: x % 2 == 0, lst1)
print(list(f))
