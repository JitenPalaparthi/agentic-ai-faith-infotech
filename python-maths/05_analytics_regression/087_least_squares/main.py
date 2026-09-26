import numpy as np
def fit_line(x,y):
    X=np.column_stack([x,np.ones_like(x)])
    m,c=np.linalg.lstsq(X,y,rcond=None)[0]
    return m,c
def main():
    x=np.array([1.,2.,3.,4.,5.]); y=np.array([3.2,4.8,7.1,9.0,11.2])
    m,c=fit_line(x,y)
    print(f"Best-fit line: y = {m:.4f}x + {c:.4f}")
if __name__=="__main__": main()
