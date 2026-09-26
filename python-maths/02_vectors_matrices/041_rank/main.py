import numpy as np
def main():
    A=np.array([[1.,2.],[2.,4.]])
    print(A); print("Rank:",np.linalg.matrix_rank(A))
if __name__=="__main__": main()
