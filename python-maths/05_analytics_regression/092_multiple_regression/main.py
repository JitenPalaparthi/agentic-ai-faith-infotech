import numpy as np
def fit(X,y):
    design=np.column_stack([np.ones(len(X)),X])
    return np.linalg.lstsq(design,y,rcond=None)[0]
def main():
    X=np.array([[1.,2.],[2.,1.],[3.,4.],[4.,3.],[5.,5.]])
    y=np.array([8.,7.,18.,17.,22.])
    print("β0, β1, β2:",fit(X,y))
if __name__=="__main__": main()
