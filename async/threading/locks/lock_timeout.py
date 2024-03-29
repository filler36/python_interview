from threading import Lock


lock = Lock()
lock.acquire()
print('after acquire')
# lock.acquire()  # This call will block main thread forever since lock is already acquired
lock.acquire(timeout=5)  # This call will block main thread forever 5 sec
print('end')
