import numpy as np
def main():
    a=np.array([1.,0.,0.]); b=np.array([0.,1.,0.])
    c=np.cross(a,b)
    print("a × b:",c)
    print("(a×b)·a:",c@a); print("(a×b)·b:",c@b)
if __name__=="__main__": main()
