import time
from threading import Thread


class Countdown:
    def __init__(self, n):
        self.n = n
        self._running = True

    def __call__(self, *args, **kwargs):
        while self._running and self.n > 0:
            print(self.n, 'left')
            self.n -= 1
            time.sleep(1)

    def terminate(self):
        self._running = False


c = Countdown(20)
t = Thread(target=c)
t.start()

time.sleep(10)
c.terminate()
