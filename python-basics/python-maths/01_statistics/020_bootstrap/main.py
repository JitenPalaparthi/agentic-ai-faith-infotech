import numpy as np

def bootstrap_means(data, repeats=2000, seed=42):
    rng = np.random.default_rng(seed)
    data = np.asarray(data, dtype=float)
    return np.array([rng.choice(data, len(data), replace=True).mean()
                     for _ in range(repeats)])

def main():
    data = [12,15,14,10,18,20,17]
    means = bootstrap_means(data)
    print("Observed mean:", np.mean(data))
    print("Bootstrap 95% percentile interval:", np.percentile(means, [2.5,97.5]))

if __name__ == "__main__":
    main()
