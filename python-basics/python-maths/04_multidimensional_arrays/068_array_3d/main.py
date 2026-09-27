import numpy as np
def main():
    X=np.arange(24).reshape(2,3,4)
    print("shape:",X.shape); print("First 3x4 matrix:\n",X[0]); print("X[1,2,3]:",X[1,2,3])
if __name__=="__main__": main()
