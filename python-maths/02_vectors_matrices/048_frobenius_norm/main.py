import numpy as np
def main():
    A=np.array([[1.,2.],[3.,4.]])
    manual=np.sqrt(np.sum(A**2))
    print("Manual:",manual); print("NumPy:",np.linalg.norm(A,"fro"))
if __name__=="__main__": main()
