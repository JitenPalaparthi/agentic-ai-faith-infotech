import numpy as np
def scale(v,k): return k*v
def main():
    v=np.array([1.,2.,3.])
    print("Original:",v); print("Scaled:",scale(v,5))
if __name__=="__main__": main()
