import numpy as np
def main():
    X=np.zeros((2,3,4))
    Y=np.transpose(X,(2,0,1))
    print("Original shape:",X.shape); print("Reordered shape:",Y.shape)
if __name__=="__main__": main()
