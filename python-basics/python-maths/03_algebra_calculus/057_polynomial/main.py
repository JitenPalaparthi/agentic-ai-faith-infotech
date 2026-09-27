import numpy as np
def main():
    x=np.array([0.,1.,2.,3.])
    coefficients=[2,-3,5]
    print("2x²-3x+5:",np.polyval(coefficients,x))
if __name__=="__main__": main()
