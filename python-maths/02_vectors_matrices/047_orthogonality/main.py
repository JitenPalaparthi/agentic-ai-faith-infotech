import numpy as np
def main():
    a=np.array([1.,0.]); b=np.array([0.,5.])
    value=a@b
    print("Dot product:",value); print("Orthogonal:",np.isclose(value,0))
if __name__=="__main__": main()
