from statistics import mean,median
from collections import Counter

import numpy as np

def arthemetic_mean(values):
    return sum(values)/len(values)

def find_mode(values):
    counts = Counter(values)
    return counts.most_common(1)[0]

def main():
    data = [10,20,30,40,50]
    print("data:",data)
    print("statistics mean:",mean(data))
    print("numnpy mean",np.mean(data))
    print("arthemetic mean:",arthemetic_mean(data))

    data = [10,20,30,40,50,6000]
    print("numnpy mean",np.mean(data))

    data.sort()
    print("statistical median:",median(data))

    data = ["A","B","A","B","C","A","B","A"]
    value,frequence = find_mode(data)
    print("Mode:",value,"Frequency:",frequence)

    data= [10,20,30,40,60,80] # 40
    print("simple  var Nunpy",np.var(data,ddof=1))
    print("population var Nunpy",np.var(data,ddof=0))






main()