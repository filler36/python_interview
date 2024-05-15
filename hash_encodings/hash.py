"""
Deterministic - hash function will always produce the same output (hash) when given the same input
Universal Input - designed to accept any kind of data as input - be it numbers, strings, etc.
Fixed-Sized Output
Fast to Compute
Uniformly Distributed - refers to the idea that a good hash function will distribute keys evenly across the array or hash table.
Randomly Distributed - hash values generated by the hash function appear to be random and lack any noticeable pattern, despite the input being structured or predictable
Randomized Seed
One-Way Function
Avalanche Effect - refers to a desired property of these functions where a small change in input (even a change in a single bit) results in a drastic, unpredictable change in the output
"""

x = 123213 ** 100
y = 123213 ** 100
print(f'IDs will not be equal: {id(x)} != {id(y)}')
print(f'Hashes will be equal: {hash(x)} == {hash(y)}')
