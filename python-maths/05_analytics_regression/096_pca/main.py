import numpy as np
def pca_directions(X):
    Xc=X-X.mean(axis=0)
    cov=np.cov(Xc,rowvar=False)
    values,vectors=np.linalg.eigh(cov)
    order=np.argsort(values)[::-1]
    return values[order],vectors[:,order]
def main():
    X=np.array([[2.5,2.4],[.5,.7],[2.2,2.9],[1.9,2.2],[3.1,3.]])
    values,vectors=pca_directions(X)
    print("Variances:",values); print("Principal directions:\n",vectors)
if __name__=="__main__": main()
