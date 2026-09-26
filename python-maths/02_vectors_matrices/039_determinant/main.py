import numpy as np
def det_2x2(A): return A[0,0]*A[1,1]-A[0,1]*A[1,0]
def main():
    A=np.array([[4.,7.],[2.,6.]])
    print("Manual determinant:",det_2x2(A)); print("NumPy:",np.linalg.det(A))
if __name__=="__main__": main()
