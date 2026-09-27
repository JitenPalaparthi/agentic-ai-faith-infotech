import numpy as np

def main():
    rng = np.random.default_rng(42)
    sample = rng.normal(loc=100, scale=15, size=10000)
    print("Sample mean:", sample.mean())
    print("Sample standard deviation:", sample.std())
    print("Approx. fraction within 1 SD:", np.mean((sample >= 85) & (sample <= 115)))

if __name__ == "__main__":
    main()
