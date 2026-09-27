import numpy as np
def line(x,m,c): return m*x+c
def main():
    x=np.arange(0,6,dtype=float); m=2.; c=3.; y=line(x,m,c)
    print(f"Equation: y = {m}x + {c}")
    for xv,yv in zip(x,y): print(f"x={xv:.0f}, y={yv:.1f}")
if __name__=="__main__": main()
