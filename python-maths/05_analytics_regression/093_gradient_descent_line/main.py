import numpy as np
def fit_gradient_descent(x,y,lr=0.01,steps=3000):
    m=c=0.0
    for _ in range(steps):
        error=(m*x+c)-y
        m-=lr*2*np.mean(error*x)
        c-=lr*2*np.mean(error)
    return m,c
def main():
    x=np.array([1.,2.,3.,4.,5.]); y=2*x+1
    print("Learned m,c:",fit_gradient_descent(x,y))
if __name__=="__main__": main()
