import numpy as np
def main():
    v=np.array([1,2,3])
    print("Original:",v.shape); print("Column:",v[:,None].shape); print("Row:",v[None,:].shape)
if __name__=="__main__": main()
