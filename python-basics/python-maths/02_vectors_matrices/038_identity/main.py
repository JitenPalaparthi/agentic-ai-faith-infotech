import numpy as np
def main():
    A=np.array([[2.,3.],[4.,5.]])
    I=np.eye(2)
    print("I:\n",I); print("A @ I:\n",A@I)
if __name__=="__main__": main()
