import numpy as np
def sigmoid(x): return 1/(1+np.exp(-x))
def main():
    x=np.array([-4.,-2.,0.,2.,4.])
    print(np.column_stack([x,sigmoid(x)]))
if __name__=="__main__": main()
