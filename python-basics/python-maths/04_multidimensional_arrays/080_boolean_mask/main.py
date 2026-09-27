import numpy as np
def main():
    X=np.arange(12).reshape(3,4)
    mask=X>6
    print("Mask:\n",mask); print("Selected:",X[mask])
if __name__=="__main__": main()
