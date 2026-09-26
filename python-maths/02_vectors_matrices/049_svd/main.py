import numpy as np
def main():
    A=np.array([[1.,2.],[3.,4.],[5.,6.]])
    U,S,Vt=np.linalg.svd(A,full_matrices=False)
    reconstructed=U@np.diag(S)@Vt
    print("Singular values:",S); print("Reconstructed:\n",np.round(reconstructed,8))
if __name__=="__main__": main()
