from threading import Thread, Lock

counter = 0
lock = Lock()

def inc():
    global counter
    for _ in range(10000):
        with lock:
            counter += 1

ts = [Thread(target=inc) for _ in range(4)]
for t in ts: t.start()
for t in ts: t.join()
print(counter)
