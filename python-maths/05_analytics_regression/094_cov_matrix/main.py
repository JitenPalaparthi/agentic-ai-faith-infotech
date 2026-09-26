import numpy as np
def main():
    X=np.array([[1.,2.,8.],[2.,4.,4.],[3.,6.,3.],[4.,8.,1.]])
    print("Covariance matrix:\n",np.cov(X,rowvar=False))
if __name__=="__main__": main()
