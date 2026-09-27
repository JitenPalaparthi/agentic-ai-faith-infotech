import numpy as np
def main():
    sales=np.array([100,120,90,150])
    print("Sales:",sales); print("Cumulative:",np.cumsum(sales))
if __name__=="__main__": main()
