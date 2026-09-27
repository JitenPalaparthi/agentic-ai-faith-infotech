def data_range(values):
    return max(values) - min(values)

def main():
    data = [12, 18, 25, 30, 41]
    print("Minimum:", min(data))
    print("Maximum:", max(data))
    print("Range:", data_range(data))

if __name__ == "__main__":
    main()
