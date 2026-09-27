import math
def sigmoid(z): return 1/(1+math.exp(-z))
for z in [-2,0,2]:
    p=sigmoid(z)
    print("z",z,"sigmoid",p,"derivative",p*(1-p))
