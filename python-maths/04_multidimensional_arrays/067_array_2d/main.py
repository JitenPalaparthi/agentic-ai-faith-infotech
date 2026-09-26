import numpy as np
def main():
    X=np.arange(12).reshape(3,4)
    print(X); print("shape:",X.shape,"ndim:",X.ndim)
    print("Second row:",X[1]); print("Third column:",X[:,2])
if __name__=="__main__": main()
