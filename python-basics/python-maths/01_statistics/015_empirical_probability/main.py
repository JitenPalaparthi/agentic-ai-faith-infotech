def empirical_probability(values, event):
    return values.count(event) / len(values)

def main():
    tosses = ["H","T","H","H","T","H","T","H"]
    print("P(H) estimated from data:", empirical_probability(tosses, "H"))

if __name__ == "__main__":
    main()
