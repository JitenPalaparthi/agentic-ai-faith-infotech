import math
x=[1,2]; y=[0,1]; b0=0.0; b1=0.0; alpha=.1
p=[1/(1+math.exp(-(b0+b1*xi))) for xi in x]
errors=[pi-yi for pi,yi in zip(p,y)]
g0=sum(errors)/len(x)
g1=sum(xi*e for xi,e in zip(x,errors))/len(x)
print("probabilities",p,"errors",errors,"gradients",g0,g1)
b0-=alpha*g0; b1-=alpha*g1
print("updated coefficients",b0,b1)
