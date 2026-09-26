from statistics import median

def main():
    regular = [10, 20, 30, 40, 50]
    with_outlier = [10, 20, 30, 40, 5000]
    print("Median without outlier:", median(regular))
    print("Median with outlier:", median(with_outlier))
    print("Mean with outlier:", sum(with_outlier) / len(with_outlier))

if __name__ == "__main__":
    main()
