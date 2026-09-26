import numpy as np
def main():
    A=np.arange(6).reshape(2,3); B=np.arange(12).reshape(3,4)
    C=np.einsum("ij,jk->ik",A,B)
    print("einsum:\n",C); print("Same as @:",np.array_equal(C,A@B))
if __name__=="__main__": main()
