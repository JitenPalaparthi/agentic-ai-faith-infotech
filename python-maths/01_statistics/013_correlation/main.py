import numpy as np

def main():
    x = np.array([1,2,3,4,5], dtype=float)
    y = np.array([2,4,5,8,10], dtype=float)
    r = np.corrcoef(x, y)[0, 1]
    print("Correlation:", r)

if __name__ == "__main__":
    main()
