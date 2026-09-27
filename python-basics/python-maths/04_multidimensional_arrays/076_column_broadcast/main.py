import numpy as np
def main():
    X=np.array([[1,2,3],[4,5,6]])
    row_offsets=np.array([[10],[20]])
    print(X+row_offsets)
if __name__=="__main__": main()
