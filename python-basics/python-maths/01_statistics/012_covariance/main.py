import numpy as np

def sample_covariance(x, y):
    x_bar, y_bar = np.mean(x), np.mean(y)
    return sum((a-x_bar)*(b-y_bar) for a,b in zip(x,y)) / (len(x)-1)

def main():
    x = [1, 2, 3, 4, 5]
    y = [2, 4, 5, 8, 10]
    print("Manual covariance:", sample_covariance(x, y))
    print("NumPy covariance matrix:\n", np.cov(x, y))

if __name__ == "__main__":
    main()
