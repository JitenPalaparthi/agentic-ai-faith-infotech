import numpy as np

def expected_value(outcomes, probabilities):
    return np.sum(np.asarray(outcomes) * np.asarray(probabilities))

def main():
    outcomes = [0, 10, 20]
    probabilities = [0.2, 0.5, 0.3]
    print("Probability sum:", sum(probabilities))
    print("Expected value:", expected_value(outcomes, probabilities))

if __name__ == "__main__":
    main()
