counter = 0


def print_ids(lst: list) -> None:
    global counter
    counter += 1
    print(f'lst{counter} id: {id(lst)}, 2 element id: {id(lst[2])}')


# Initial list
lst1 = [1, 2, [3, 4]]
print_ids(lst1)

# This doesn't actually create a second list. The assignment just copies the reference to the list,
# not the actual list, so both lst1 and lst2 refer to the same list after the assignment.
lst2 = lst1
print_ids(lst2)

# To actually copy the list, you have several options:
# You can use the builtin list.copy() method (available since Python 3.3):
lst3 = lst1.copy()
print_ids(lst3)

# You can make it with slice:
lst4 = lst1[:]
print_ids(lst4)

# You can use the built in list() constructor:
lst5 = list(lst1)
print_ids(lst5)

# You can use generic copy.copy():
import copy
lst6 = copy.copy(lst1)  # This is a little slower than list() because it has to find out the datatype of old_list first
print_ids(lst6)

# If you need to copy the elements of the list as well, use generic copy.deepcopy()
# Obviously the slowest and most memory-needing method, but sometimes unavoidable
# This operates recursively; it will handle any number of levels of nested lists (or other containers)
lst7 = copy.deepcopy(lst1)
print_ids(lst7)
