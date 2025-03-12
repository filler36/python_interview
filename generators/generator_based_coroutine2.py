def coroutine():
    x = [1, 2]
    for i in x:
        yield i # A
        z = yield # B
        if z:
            yield z


c = coroutine()
i = iter(c)
print(next(i)) # yields 1 and pauses at A
next(i) # yields None and pauses at B
print(i.send('test')) # sends 'test' after yield at B, yields z and pauses
print(next(i)) # yields 2 and pauses at A
print(next(i)) # yields None
