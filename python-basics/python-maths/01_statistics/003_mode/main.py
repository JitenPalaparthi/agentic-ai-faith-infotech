from collections import Counter

def find_mode(values):
    counts = Counter(values)
    return counts.most_common(1)[0]

def main():
    data = ["A", "B", "A", "C", "A", "B","B"]
    value, frequency = find_mode(data)
    print("Frequencies:", Counter(data))
    print("Mode:", value, "Frequency:", frequency)

if __name__ == "__main__":
    main()
