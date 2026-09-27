import math
row_probs=[.8,.7]
ll=sum(math.log(q) for q in row_probs)
print("log likelihood =",ll)
