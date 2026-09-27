from statistics import mean
import numpy as np

def arithmetic_mean(values):
    return sum(values) / len(values)

def main():
    data = [10, 20, 30, 40, 50]
    print("Data:", data)
    print("Manual formula:", arithmetic_mean(data))
    print("statistics.mean:", mean(data))
    print("numpy.mean:", np.mean(data))

if __name__ == "__main__":
    main()
