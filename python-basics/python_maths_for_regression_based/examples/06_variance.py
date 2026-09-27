x=[0,5,10]
mean=sum(x)/len(x)
dev=[v-mean for v in x]
sq=[d*d for d in dev]
variance=sum(sq)/len(x)
print("mean:",mean); print("deviations:",dev); print("squares:",sq); print("population variance:",variance)
