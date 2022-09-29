"""
Dict implementation before Python 3.6
"""

dict1 = dict()  # Create hashtable with 8 slots. Each slot in the table can store one and only one entry
'''
hashtable is just a contiguous block of memory (like an array, so you can do O(1) lookup by index):
[   ],
[   ],
[   ],
[   ],
[   ],
[   ],
[   ],
[   ],
'''

# Add key-value to the dict
dict1['name'] = 'Filip'
'''
HASH = hash('name') -> 'name'.__hash__() -> Example: 7523062142597211918 ->
-> 0b110100001100111010010010010100011101000101100100010011100001110 - hash of 'name' represented in binary
MASK = N - 1 = 7(decimal) = 111(binary), where N is number of slots/buckets
BUCKET_INDEX = HASH & MASK, where & is BITWISE AND operator
BUCKET_INDEX = 0b110100001100111010010010010100011101000101100100010011100001110 & 111 = 111(binary) = 5(decimal)
hashtable:
[   ],
[   ],
[   ],
[   ],
[   ],
[HASH, <ref to key 'name' in memory>, <ref to value 'Filip' in memory>],
[   ],
[   ],
'''

# Let's add another key-value to the dict
dict1['age'] = 33
'''
HASH = hash('age') -> 'age'.__hash__() -> Example: 9109825798157558154 ->
-> 0b111111001101100100110100100110000101000110111101110000110001010 - hash of 'age' represented in binary
MASK = N - 1 = 7(decimal) = 111(binary), where N is number of slots/buckets
BUCKET_INDEX = HASH & MASK, where & is BITWISE AND operator
BUCKET_INDEX = 0b111111001101100100110100100110000101000110111101110000110001010 & 111 = 010(binary) = 2(decimal)
hashtable:
[   ],
[   ],
[HASH, <ref to key 'age' in memory>, <ref to value 33 in memory>],
[   ],
[   ],
[HASH, <ref to key 'name' in memory>, <ref to value 'Filip' in memory>],
[   ],
[   ],
'''

# And one more key-value to the dict, that will give us collision
dict1['country'] = 'Poland'
'''
HASH = hash('country') -> 'country'.__hash__() -> Example: -9044573126986865771 ->
-> -0b111110110000100110001110101011010111011000110001001110001101011 - hash of 'country' represented in binary
MASK = N - 1 = 7(decimal) = 111(binary), where N is number of slots/buckets
BUCKET_INDEX = HASH & MASK, where & is BITWISE AND operator
BUCKET_INDEX = -0b111110110000100110001110101011010111011000110001001110001101011 & 111 = 101(binary) = 5(decimal)
Rule for negative binary: -011. Invert bits: 100. Add 1: 101. Calculate 101 & 111 = 101(binary) = 5(decimal)
So now we have collision, because bucket with index 5 is already occupied.
If the slot is occupied, CPython (and even PyPy) compares the hash and the key (by compare I mean == comparison
not the is comparison) of the entry in the slot against the key of the current entry to be inserted

If both match, then it thinks the entry with such key already exists.
In case the new value are same it just do nothing.
Otherwise, it creates new object in memory and update reference to that new object

If either hash or the key don't match, it starts probing. Probing just means it searches the slots by slot to find
an empty slot. Technically we could just go one by one, i+1, i+2, ... and use the first available one (that's linear
probing). But for reasons explained beautifully in the comments (see dictobject.c:33-126),
CPython uses random probing. In random probing, the next slot is picked in a pseudo random order. The entry is added
to the first empty slot. For this discussion, the actual algorithm used to pick the next slot is not really important
(see dictobject.c:33-126 for the algorithm for probing). What is important is that the slots are probed until first
empty slot is found.

The same thing happens for lookups, just starts with the initial slot i (where i depends on the hash of the key).
If the hash and the key both don't match the entry in the slot, it starts probing,
until it finds a slot with a match. If all slots are exhausted, it reports a fail.

To avoid slowing down lookups, the dict will be resized when it is two-thirds full

hashtable:
[   ],
[   ],
[HASH, <ref to key 'age' in memory>, <ref to value 33 in memory>],
[   ],
[   ],
[HASH, <ref to key 'name' in memory>, <ref to value 'Filip' in memory>],
[   ],
[HASH, <ref to key 'country' in memory>, <ref to value 'Poland' in memory>],
'''

# Add more and more key-value pairs
dict1['phone_number_1'] = '111-111-111'
dict1['phone_number_2'] = '222-222-222'
dict1['phone_number_2'] = '333-333-333'
'''
After 5 key-values are stored, the probability of hash collisions is too large,
so the dictionary will be doubled in size.

hashtable:
[HASH, <ref to key 'phone_number_1' in memory>, <ref to value '111-111-111' in memory>],
[   ],
[HASH, <ref to key 'age' in memory>, <ref to value 33 in memory>],
[HASH, <ref to key 'phone_number_2' in memory>, <ref to value '222-222-222' in memory>],
[   ],
[HASH, <ref to key 'name' in memory>, <ref to value 'Filip' in memory>],
[HASH, <ref to key 'phone_number_3' in memory>, <ref to value '333-333-333' in memory>],
[HASH, <ref to key 'country' in memory>, <ref to value 'Poland' in memory>],
[   ],
[   ],
[   ],
[   ],
[   ],
[   ],
[   ],
[   ],
'''
