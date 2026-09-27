weights=[3,-2,1]
lam=.1
l2=lam*sum(w*w for w in weights)
l1=lam*sum(abs(w) for w in weights)
print("weights",weights,"L2 penalty",l2,"L1 penalty",l1)
