import numpy as np
def standardize(X):
    X=np.asarray(X,dtype=float); return (X-X.mean(axis=0))/X.std(axis=0)
def main():
    X=np.array([[10.,100.],[20.,120.],[30.,140.]])
    Z=standardize(X); print(Z); print("Means:",Z.mean(0)); print("SDs:",Z.std(0))
if __name__=="__main__": main()
