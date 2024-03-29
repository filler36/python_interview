import threading
"""
The file is being written by two threads simultaneously without any synchronization mechanism like locks.
This is a race condition
"""


def worker(x):
    fp = open('file_write_race_condition.txt', 'a')
    for i in range(100000):
        fp.write(x)
    fp.close()


t1 = threading.Thread(target=worker, args=('1',))
t2 = threading.Thread(target=worker, args=('2',))
t1.start()
t2.start()
