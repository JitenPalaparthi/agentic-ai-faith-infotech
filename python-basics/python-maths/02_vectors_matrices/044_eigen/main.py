import numpy as np
def main():
    A=np.array([[2.,0.],[0.,3.]])
    values,vectors=np.linalg.eig(A)
    print("Eigenvalues:",values); print("Eigenvectors:\n",vectors)
    v=vectors[:,0]; print("Check Av:",A@v); print("Check λv:",values[0]*v)
if __name__=="__main__": main()
