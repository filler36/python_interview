t1 = (1, 2, 3)
t2 = (1, 2, [3, 4])  # It is possible to create tuple with mutable element (for example list)

# However, hash from that tuple will raise TypeError exception
print(hash(t1))
print(hash(t2))  # TypeError: unhashable type: 'list'
