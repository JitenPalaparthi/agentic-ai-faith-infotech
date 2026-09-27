import math
def sigmoid(z): return 1/(1+math.exp(-z))
for z in [-2,0,2]:
    print(z, sigmoid(z))
