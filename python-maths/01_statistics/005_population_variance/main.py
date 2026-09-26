import numpy as np

def population_variance(values):
    mean = sum(values) / len(values)
    return sum((x - mean) ** 2 for x in values) / len(values)

def main():
    data = [10, 20, 30, 40, 50]
    print("Manual variance:", population_variance(data))
    print("NumPy variance:", np.var(data))

if __name__ == "__main__":
    main()
