import threading
import time


def worker():
    time.sleep(2)
    print("DONE")


t1 = threading.Thread(target=worker)
t1.start()
t2 = threading.Thread(target=worker)
t2.start()
t3 = threading.Thread(target=worker)
t3.start()
