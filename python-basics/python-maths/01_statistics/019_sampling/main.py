import numpy as np

def main():
    rng = np.random.default_rng(42)
    population = np.arange(1, 1001)
    sample = rng.choice(population, size=20, replace=False)
    print("Sample:", sample)
    print("Sample mean:", sample.mean())

if __name__ == "__main__":
    main()
