import numpy as np
def main():
    images=np.zeros((8,64,64,3),dtype=np.float32)
    print("shape:",images.shape); print("ndim:",images.ndim); print("MB:",images.nbytes/1024**2)
if __name__=="__main__": main()
