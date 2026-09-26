import numpy as np
def pairwise_distances(points):
    diff=points[:,None,:]-points[None,:,:]
    return np.sqrt(np.sum(diff**2,axis=2))
def main():
    P=np.array([[0.,0.],[3.,4.],[6.,8.]])
    print(pairwise_distances(P))
if __name__=="__main__": main()
