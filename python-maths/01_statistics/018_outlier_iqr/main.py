import numpy as np

def find_outliers(values):
    q1, q3 = np.percentile(values, [25,75])
    iqr = q3-q1
    lower, upper = q1-1.5*iqr, q3+1.5*iqr
    values = np.asarray(values)
    return lower, upper, values[(values < lower) | (values > upper)]

def main():
    data = [10,11,12,13,14,15,100]
    lower, upper, outliers = find_outliers(data)
    print("Bounds:", lower, upper)
    print("Potential outliers:", outliers)

if __name__ == "__main__":
    main()
