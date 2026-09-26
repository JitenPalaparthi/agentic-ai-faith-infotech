def f(x,y): return x*x+3*y*y
def partial_x(x,y,h=1e-5): return (f(x+h,y)-f(x-h,y))/(2*h)
def partial_y(x,y,h=1e-5): return (f(x,y+h)-f(x,y-h))/(2*h)
def main():
    x,y=2.,1.
    print("Gradient approximation:",[partial_x(x,y),partial_y(x,y)])
    print("Exact gradient:",[2*x,6*y])
if __name__=="__main__": main()
