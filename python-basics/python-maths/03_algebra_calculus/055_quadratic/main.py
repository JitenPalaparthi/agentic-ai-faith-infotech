import numpy as np
def quadratic(x,a,b,c): return a*x**2+b*x+c
def main():
    x=np.arange(-3,4,dtype=float)
    print("x:",x); print("y:",quadratic(x,1,2,-3))
if __name__=="__main__": main()
