import numpy as np
def main():
    A=np.array([[4.,7.],[2.,6.]])
    inv=np.linalg.inv(A)
    print("Inverse:\n",inv); print("Verification:\n",A@inv)
if __name__=="__main__": main()
