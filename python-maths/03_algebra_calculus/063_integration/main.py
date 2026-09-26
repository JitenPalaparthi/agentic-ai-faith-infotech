import numpy as np
def main():
    x=np.linspace(0,2,10001); y=x**2
    area=np.trapezoid(y,x)
    print("Approx integral of x² from 0 to 2:",area)
    print("Exact value 8/3:",8/3)
if __name__=="__main__": main()
