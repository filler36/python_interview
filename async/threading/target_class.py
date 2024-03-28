import threading
import time
from threading import Thread


class Countdown:
    def __init__(self, n):
        self.n = n

    def __call__(self, *args, **kwargs):
        for i in range(self.n):
            print(self.n - i - 1, 'left')
            time.sleep(1)


t = Thread(target=Countdown(5), name='First thread')  # We can set Thread name
print(t.name)  # First thread will be printed
print(t.ident)  # Unique identificator of the thread = None -> It will be set after starting
print(threading.enumerate())  # [<_MainThread(MainThread, started 21468)>]
t.start()
print(t.ident)  # Unique identificator of the thread
print(threading.enumerate())  # [<_MainThread(MainThread, started 35528)>, <Thread(First thread, started 2072)>]
