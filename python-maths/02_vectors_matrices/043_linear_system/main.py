import numpy as np
def main():
    A=np.array([[2.,1.],[1.,3.]])
    b=np.array([8.,13.])
    x=np.linalg.solve(A,b)
    print("Solution x:",x); print("Check Ax:",A@x); print("b:",b)
if __name__=="__main__": main()
