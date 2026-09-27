import numpy as np
def dot(a,b):
    if a.shape!=b.shape: raise ValueError("Same dimension required")
    return float(np.dot(a,b))
def main():
    a=np.array([1.,2.,3.]); b=np.array([4.,5.,6.])
    print("a:",a); print("b:",b)
    print("Dot product:",dot(a,b))
    print("Manual:",1*4+2*5+3*6)
if __name__=="__main__": main()
