def f(x): return (x-3)**2
def grad(x): return 2*(x-3)
def minimize(start,lr=0.1,steps=30):
    x=start
    for _ in range(steps): x=x-lr*grad(x)
    return x
def main():
    x=minimize(20.)
    print("Estimated minimizer:",x); print("f(x):",f(x))
if __name__=="__main__": main()
