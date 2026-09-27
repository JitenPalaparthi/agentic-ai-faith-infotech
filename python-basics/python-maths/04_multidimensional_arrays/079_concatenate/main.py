import numpy as np
def main():
    A=np.ones((2,2)); B=np.zeros((2,1))
    C=np.concatenate([A,B],axis=1)
    print(C); print("Shape:",C.shape)
if __name__=="__main__": main()
