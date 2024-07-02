import copy


a1 = [[1, 2, 3], 4, 5]
a2 = copy.copy(a1)
a3 = copy.deepcopy(a1)


print(id(a1))
print(id(a2))  # Shallow copy with different id
print(id(a3))  # Deep copy with different id

print()

print(id(a1[0]))
print(id(a2[0]))  # This nested element will not be copied since it is shallow copy
print(id(a3[0]))  # Completely new object
