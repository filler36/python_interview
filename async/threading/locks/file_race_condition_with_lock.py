import threading


def worker(x):
    with lock:
        fp = open('file_write_lock.txt', 'a')
        for i in range(100000):
            fp.write(x)
        fp.close()

lock = threading.Lock()
t1 = threading.Thread(target=worker, args=('1',))
t2 = threading.Thread(target=worker, args=('2',))
t1.start()
t2.start()
