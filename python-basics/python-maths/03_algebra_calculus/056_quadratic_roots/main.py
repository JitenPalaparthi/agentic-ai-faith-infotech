import math
def roots(a,b,c):
    d=b*b-4*a*c
    if d<0: return ()
    return ((-b+math.sqrt(d))/(2*a),(-b-math.sqrt(d))/(2*a))
def main():
    print("Roots of x²-5x+6:",roots(1,-5,6))
if __name__=="__main__": main()
