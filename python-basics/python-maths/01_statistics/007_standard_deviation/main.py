import math
import numpy as np

def population_std(values):
    mean = sum(values) / len(values)
    variance = sum((x - mean) ** 2 for x in values) / len(values)
    return math.sqrt(variance)

def main():
    data = [10, 20, 30, 40, 50]
    print("Manual standard deviation:", population_std(data))
    print("NumPy standard deviation:", np.std(data))

if __name__ == "__main__":
    main()
