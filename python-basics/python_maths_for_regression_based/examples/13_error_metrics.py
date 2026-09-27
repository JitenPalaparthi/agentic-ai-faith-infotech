import math
y=[2,3,5]; pred=[2,4,4]
errors=[a-b for a,b in zip(y,pred)]
sq=[e*e for e in errors]
sse=sum(sq); mse=sse/len(y); rmse=math.sqrt(mse)
print("errors",errors,"squared",sq); print("SSE",sse,"MSE",mse,"RMSE",rmse)
