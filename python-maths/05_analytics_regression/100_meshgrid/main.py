import numpy as np
def main():
    x=np.linspace(-2,2,5); y=np.linspace(-2,2,5)
    X,Y=np.meshgrid(x,y); Z=X**2+Y**2
    print("X:\n",X); print("Y:\n",Y); print("Z=x²+y²:\n",Z)
if __name__=="__main__": main()
