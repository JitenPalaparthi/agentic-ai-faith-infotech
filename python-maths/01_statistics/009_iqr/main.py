import numpy as np

def main():
    data = np.array([2, 4, 5, 7, 8, 9, 10, 30])
    q1, q3 = np.percentile(data, [25, 75])
    print("Q1:", q1)
    print("Q3:", q3)
    print("IQR:", q3 - q1)

if __name__ == "__main__":
    main()
