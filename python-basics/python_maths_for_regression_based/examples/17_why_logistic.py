# A line is not constrained to valid probabilities.
def linear_score(x): return -0.5 + 0.6*x
for x in [-2,0,1,3,5]:
    print(x, linear_score(x))
