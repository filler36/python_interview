import time
from threading import Thread


class Countdown:
    def __init__(self, n):
        self.n = n

    def __call__(self, *args, **kwargs):
        for i in range(self.n):
            print(self.n - i - 1, 'left')
            time.sleep(1)


t = Thread(target=Countdown(5))
t.start()
