import numpy as np

def main():
    rng = np.random.default_rng(42)
    n, p = 10, 0.6
    samples = rng.binomial(n=n, p=p, size=10000)
    print("Theoretical mean:", n*p)
    print("Simulated mean:", samples.mean())

if __name__ == "__main__":
    main()
