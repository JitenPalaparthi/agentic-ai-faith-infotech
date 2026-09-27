from concurrent.futures import ThreadPoolExecutor

def square(x): return x*x

with ThreadPoolExecutor(max_workers=4) as ex:
    print(list(ex.map(square, range(8))))
