x=[1,2,3,4,5]; y=[2,3,5,4,6]
xm=sum(x)/len(x); ym=sum(y)/len(y)
num=sum((a-xm)*(b-ym) for a,b in zip(x,y))
den=sum((a-xm)**2 for a in x)
b1=num/den; b0=ym-b1*xm
print("xbar",xm,"ybar",ym,"numerator",num,"denominator",den)
print("slope",b1,"intercept",b0)
print("predictions",[b0+b1*a for a in x])
