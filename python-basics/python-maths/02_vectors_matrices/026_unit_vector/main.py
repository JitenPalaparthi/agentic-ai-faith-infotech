import numpy as np
def unit_vector(v):
    norm=np.linalg.norm(v)
    if norm==0: raise ValueError("Zero vector has no direction")
    return v/norm
def main():
    v=np.array([3.,4.]); u=unit_vector(v)
    print("Unit vector:",u); print("Magnitude:",np.linalg.norm(u))
if __name__=="__main__": main()
