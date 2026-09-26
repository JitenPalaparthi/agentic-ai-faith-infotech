import numpy as np

def sample_variance(values):
    mean = sum(values) / len(values)
    return sum((x - mean) ** 2 for x in values) / (len(values) - 1)

def main():
    data = [10, 20, 30, 40, 50]
    print("Manual sample variance:", sample_variance(data))
    print("NumPy ddof=1:", np.var(data, ddof=1))

if __name__ == "__main__":
    main()
