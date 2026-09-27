import numpy as np
def main():
    data=np.array([1,1,2,2,2,3,4,5,5,5,6])
    counts,edges=np.histogram(data,bins=5)
    print("Bin edges:",edges); print("Counts:",counts)
if __name__=="__main__": main()
