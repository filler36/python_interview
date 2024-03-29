import threading
import time


def worker(x):
    time.sleep(x)
    print("DONE")


t1 = threading.Thread(target=worker, args=(3,))
t2 = threading.Thread(target=worker, args=(4,))
t3 = threading.Thread(target=worker, args=(5,))
t1.start()
t2.start()
t3.start()

print('END')  # Will be printed immediately before threads done their tasks


# t1.join()
# print('END')  # Will be printed only after t1 done his task
