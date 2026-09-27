from concurrent.futures import ProcessPoolExecutor

def square(x): return x*x

if __name__ == "__main__":
    with ProcessPoolExecutor() as ex:
        print(list(ex.map(square, range(8))))
