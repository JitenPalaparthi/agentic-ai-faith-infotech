import numpy as np
def main():
    x=np.arange(12); X=x.reshape(3,4)
    print("Original:",x); print("Reshaped:\n",X)
if __name__=="__main__": main()
