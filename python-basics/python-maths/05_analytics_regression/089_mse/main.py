import numpy as np
def mse(actual,predicted):
    return np.mean((np.asarray(actual)-np.asarray(predicted))**2)
def main(): print("MSE:",mse([3,5,7,9],[2.8,5.2,6.7,9.1]))
if __name__=="__main__": main()
