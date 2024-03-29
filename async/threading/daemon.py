import time
from threading import Thread


t = Thread(target=time.sleep, args=(10, ), daemon=True)
t.start()
time.sleep(5)
print(t.daemon)

#  Daemon threads will be closed automatically when the main thread finish his execution.