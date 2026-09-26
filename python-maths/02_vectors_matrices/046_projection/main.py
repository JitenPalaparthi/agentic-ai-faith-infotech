import numpy as np
def project(b,a): return (b@a)/(a@a)*a
def main():
    a=np.array([2.,1.]); b=np.array([3.,4.])
    print("Projection of b onto a:",project(b,a))
if __name__=="__main__": main()
