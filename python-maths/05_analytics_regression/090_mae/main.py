import numpy as np
def mae(actual,predicted):
    return np.mean(np.abs(np.asarray(actual)-np.asarray(predicted)))
def main(): print("MAE:",mae([3,5,7,9],[2.8,5.2,6.7,9.1]))
if __name__=="__main__": main()
