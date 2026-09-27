import numpy as np
def plane(x,y,a,b,c): return a*x+b*y+c
def main():
    x=np.array([0.,1.,2.]); y=np.array([0.,1.,2.])
    print("z:",plane(x,y,2.,3.,1.))
if __name__=="__main__": main()
