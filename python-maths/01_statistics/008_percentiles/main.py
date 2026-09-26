import numpy as np

def main():
    data = np.arange(1, 101)
    for p in (25, 50, 75, 90):
        print(f"P{p} =", np.percentile(data, p))

if __name__ == "__main__":
    main()
