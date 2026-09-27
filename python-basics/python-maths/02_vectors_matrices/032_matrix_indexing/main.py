import numpy as np
def main():
    A=np.arange(1,10).reshape(3,3)
    print(A); print("A[1,2]:",A[1,2]); print("Row 1:",A[1,:]); print("Column 1:",A[:,1])
if __name__=="__main__": main()
