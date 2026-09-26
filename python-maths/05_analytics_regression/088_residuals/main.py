import numpy as np
def main():
    x=np.array([1.,2.,3.,4.]); y=np.array([3.1,4.9,7.2,8.8])
    pred=2*x+1; residuals=y-pred
    print("Predictions:",pred); print("Residuals:",residuals); print("Residual sum:",residuals.sum())
if __name__=="__main__": main()
