import numpy as np
def distance(p,q): return np.linalg.norm(np.asarray(q)-np.asarray(p))
def main():
    print("Distance:",distance([1.,2.],[4.,6.]))
if __name__=="__main__": main()
