import numpy as np, math
def magnitude(v): return math.sqrt(sum(x*x for x in v))
def main():
    v=np.array([3.,4.])
    print("Manual:",magnitude(v)); print("NumPy:",np.linalg.norm(v))
if __name__=="__main__": main()
