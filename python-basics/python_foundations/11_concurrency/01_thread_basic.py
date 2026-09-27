from threading import Thread

def worker(n):
    print("worker", n)

threads = [Thread(target=worker, args=(i,)) for i in range(3)]
for t in threads: t.start()
for t in threads: t.join()
