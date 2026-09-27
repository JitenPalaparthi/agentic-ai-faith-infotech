x=[1,2,3]; y=[2,4,6]
xm=sum(x)/len(x); ym=sum(y)/len(y)
products=[(a-xm)*(b-ym) for a,b in zip(x,y)]
cov=sum(products)/len(x)
print("x mean:",xm,"y mean:",ym); print("products:",products); print("covariance:",cov)
