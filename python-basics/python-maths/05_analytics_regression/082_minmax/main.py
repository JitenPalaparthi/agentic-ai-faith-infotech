import numpy as np
def minmax(x):
    x=np.asarray(x,dtype=float); return (x-x.min())/(x.max()-x.min())
def main(): print(minmax([10,20,30,40]))
if __name__=="__main__": main()
