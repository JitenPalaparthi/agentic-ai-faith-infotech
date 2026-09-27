from queue import Queue
from threading import Thread

q = Queue()

def worker():
    while True:
        item = q.get()
        if item is None:
            q.task_done()
            break
        print("processing", item)
        q.task_done()

t = Thread(target=worker)
t.start()
for i in range(3): q.put(i)
q.put(None)
q.join()
t.join()
