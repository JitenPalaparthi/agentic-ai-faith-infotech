import numpy as np
def main():
    X=np.arange(24).reshape(2,3,4)
    print("Shape:",X.shape); print("Mean per batch:",X.mean(axis=(1,2)))
if __name__=="__main__": main()
