import math
for p in [.9,.1]:
    y=1
    loss=-(y*math.log(p)+(1-y)*math.log(1-p))
    print("y=1, p=",p,"loss=",loss)
