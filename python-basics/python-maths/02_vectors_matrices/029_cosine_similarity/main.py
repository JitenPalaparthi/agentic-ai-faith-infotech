import numpy as np
def cosine_similarity(a,b):
    return float((a@b)/(np.linalg.norm(a)*np.linalg.norm(b)))
def main():
    a=np.array([1.,2.,3.]); b=np.array([2.,4.,6.])
    print("Cosine similarity:",cosine_similarity(a,b))
if __name__=="__main__": main()
