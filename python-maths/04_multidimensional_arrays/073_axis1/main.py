import numpy as np
def main():
    X=np.array([[1,2,3],[4,5,6]])
    print("Row sums:",X.sum(axis=1)); print("Row means:",X.mean(axis=1))
if __name__=="__main__": main()
