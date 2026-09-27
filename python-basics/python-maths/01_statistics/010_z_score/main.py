import numpy as np

def z_scores(values):
    values = np.asarray(values, dtype=float)
    return (values - values.mean()) / values.std()

def main():
    data = np.array([10, 20, 30, 40, 50], dtype=float)
    print("Data:", data)
    print("Z-scores:", np.round(z_scores(data), 3))

if __name__ == "__main__":
    main()
