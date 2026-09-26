import numpy as np

def weighted_mean(values, weights):
    return sum(v * w for v, w in zip(values, weights)) / sum(weights)

def main():
    marks = [70, 80, 90]
    weights = [1, 2, 3]
    print("Manual weighted mean:", weighted_mean(marks, weights))
    print("NumPy weighted mean:", np.average(marks, weights=weights))

if __name__ == "__main__":
    main()
