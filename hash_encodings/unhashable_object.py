class UnhashableClass:
    __hash__ = None

    def __init__(self, x, y):
        self.x = x
        self.y = y


u = UnhashableClass(1, 2)
print(hash(u))  # TypeError: unhashable type: 'UnhashableClass'
