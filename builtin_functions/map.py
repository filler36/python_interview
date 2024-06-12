"""
Return an iterator that applies function to every item of iterable, yielding the results.
If additional iterables arguments are passed, function must take that many arguments and is applied to the items from all iterables in parallel.
With multiple iterables, the iterator stops when the shortest iterable is exhausted"""

lst1 = [1, 2, 3, 4, 5]
m = map(lambda x: x*x, lst1)
for i in m:
    print(i)

print('-----------')

lst2 = [1, 2, 3, 4, 5]
m = map(lambda x, y: x+y, lst1, lst1)
for i in m:
    print(i)
