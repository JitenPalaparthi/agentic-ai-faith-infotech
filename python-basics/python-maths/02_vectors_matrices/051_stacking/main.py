import numpy as np
def main():
    A=np.array([[1,2],[3,4]]); B=np.array([[5,6],[7,8]])
    print("Vertical:\n",np.vstack([A,B])); print("Horizontal:\n",np.hstack([A,B]))
if __name__=="__main__": main()
