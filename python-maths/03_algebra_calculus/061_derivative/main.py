def derivative(f,x,h=1e-5): return (f(x+h)-f(x-h))/(2*h)
def main():
    f=lambda x:x**2
    print("Numerical derivative at x=3:",derivative(f,3.0))
    print("Exact derivative 2x:",6.0)
if __name__=="__main__": main()
