import numpy as np
def add_vectors(a,b):
    if a.shape!=b.shape: raise ValueError("Same shape required")
    return a+b
def main():
    a=np.array([1.,2.,3.]); b=np.array([4.,5.,6.])
    print("a+b =",add_vectors(a,b))
if __name__=="__main__": main()
