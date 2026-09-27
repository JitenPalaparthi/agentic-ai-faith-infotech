import numpy as np
def main():
    X=np.array([[1,2,3],[4,5,6]])
    print("Column sums:",X.sum(axis=0)); print("Column means:",X.mean(axis=0))
if __name__=="__main__": main()
