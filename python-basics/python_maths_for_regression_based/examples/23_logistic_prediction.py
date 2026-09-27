import math
b0=-1; b1=.8; x=3
z=b0+b1*x
p=1/(1+math.exp(-z))
print("z =",z,"probability =",p)
