import threading
import time


shared_resource = []

condition = threading.Condition()


def consumer():
    with condition:
        while not shared_resource:
            print("Consumer is waiting...")
            condition.wait()
        item = shared_resource.pop(0)
        print("Consumer consumed item:", item)


def producer():
    with condition:
        time.sleep(2)
        item = "New item"
        shared_resource.append(item)
        print("Producer produced item:", item)
        time.sleep(2)
        condition.notify()


consumer_thread = threading.Thread(target=consumer)
producer_thread = threading.Thread(target=producer)
consumer_thread.start()
producer_thread.start()
