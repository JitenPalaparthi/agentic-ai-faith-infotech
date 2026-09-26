import numpy as np
def multiply(A,B):
    if A.shape[1]!=B.shape[0]: raise ValueError("Inner dimensions must match")
    return A@B
def main():
    A=np.array([[1,2,3],[4,5,6]])
    B=np.array([[7,8],[9,10],[11,12]])
    C=multiply(A,B)
    print("A shape:",A.shape,"B shape:",B.shape)
    print("A @ B:\n",C); print("Result shape:",C.shape)
if __name__=="__main__": main()
