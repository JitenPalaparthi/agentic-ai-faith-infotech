import numpy as np
def main():
    A=np.array([[1,1],[1,0]],dtype=int)
    print("A^5 (matrix power):\n",np.linalg.matrix_power(A,5))
    print("A**5 (element-wise):\n",A**5)
if __name__=="__main__": main()
