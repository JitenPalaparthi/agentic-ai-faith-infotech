import numpy as np
def main():
    X=np.array([[10,20,30],[40,50,60]])
    offset=np.array([1,2,3])
    print("X + feature offsets:\n",X+offset)
if __name__=="__main__": main()
