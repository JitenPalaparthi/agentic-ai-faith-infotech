import numpy as np
def main():
    X=np.arange(12).reshape(3,4)
    print("ravel:",X.ravel()); print("flatten:",X.flatten())
if __name__=="__main__": main()
