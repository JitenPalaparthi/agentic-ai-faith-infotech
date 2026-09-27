actual=[1,1,0,0,1]; pred=[1,0,0,1,1]
tp=sum(a==1 and p==1 for a,p in zip(actual,pred))
tn=sum(a==0 and p==0 for a,p in zip(actual,pred))
fp=sum(a==0 and p==1 for a,p in zip(actual,pred))
fn=sum(a==1 and p==0 for a,p in zip(actual,pred))
print("TP",tp,"TN",tn,"FP",fp,"FN",fn)
