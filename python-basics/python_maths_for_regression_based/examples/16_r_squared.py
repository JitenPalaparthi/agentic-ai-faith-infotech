y=[2,3,5]; pred=[2.2,3.1,4.6]
ym=sum(y)/len(y)
sse=sum((a-b)**2 for a,b in zip(y,pred))
sst=sum((a-ym)**2 for a in y)
print("SSE",sse,"SST",sst,"R2",1-sse/sst)
