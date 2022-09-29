"""
Dict implementation after Python 3.6
"""

dict1 = dict()
'''
We start, instead, by preallocating an array for the index of the insertion.
order_list:
[null, null, null, null, null, null, null, null]
'''
# Add key-value to the dict
dict1['name'] = 'Filip'
'''
Since our first key-value pair goes in the fifths slot/bucket, we index like this:

order_list:
[null, null, null, null, null, 0, null, null]

hashtable:
[HASH, <ref to key 'name' in memory>, <ref to value 'Filip' in memory>],
'''

# Let's add another key-value to the dict
dict1['age'] = 33
'''
Since this pair goes in the second slot/bucket

order_list:
[null, null, 1, null, null, 0, null, null]

hashtable:
[HASH, <ref to key 'name' in memory>, <ref to value 'Filip' in memory>],
[HASH, <ref to key 'age' in memory>, <ref to value 33 in memory>],
'''