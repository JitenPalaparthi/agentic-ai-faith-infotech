import numpy as np
def r_squared(y,p):
    y=np.asarray(y,dtype=float); p=np.asarray(p,dtype=float)
    return 1-np.sum((y-p)**2)/np.sum((y-y.mean())**2)
def main(): print("R²:",r_squared([3,5,7,9],[2.8,5.2,6.7,9.1]))
if __name__=="__main__": main()
