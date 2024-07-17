class HashableExample:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __hash__(self):
        return hash((self.x, self.y))

    """
    You also need to define __eq__() in a compatible way with __hash__() – otherwise, equality will be based on object identity.
    Indeed, after checking if the hashes are equal, the dict/set must also check for actual equality in case of hash collision
    """
    # def __eq__(self, other):
    #     if not isinstance(other, type(self)): return NotImplemented
    #     return self.x == other.x and self.y == other.y


h1 = HashableExample(1, 2)
h2 = HashableExample(1, 2)
d = {}
d[h1] = 1
d[h2] = 2
print(d)  # {<__main__.HashableExample object at 0x0000025D1A829790>: 1, <__main__.HashableExample object at 0x0000025D1A3154D0>: 2}
