"""
Coroutines are similar to generators, in that they can be stopped and paused and restarted,
but they’re different in the sense that generators generate values and then coroutines consume values.
"""


def myfunc():
    x = ''
    while True:
        print(f'Yielding x ({x}) and waiting...')
        x = yield x
        if x is None:
            break
        print(f'Got x {x}. Doubling.')
        x = x * 2


g = myfunc()
next(g)  # Yielding x () and waiting...

g.send(10)  # Got x 10. Doubling.
            # Yielding x (20) and waiting...

g.send(123)  # Got x 123 Doubling.
             # Yielding x (246) and waiting...

# g.throw(BaseException) # BaseException

# g.close()
# g.send(124)  # StopIteration

g.send(None)  # StopIteration
