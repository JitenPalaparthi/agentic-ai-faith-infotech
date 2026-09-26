def slope(p1,p2):
    x1,y1=p1; x2,y2=p2
    if x2==x1: raise ValueError("Vertical line has undefined slope")
    return (y2-y1)/(x2-x1)
def main():
    print("Slope:",slope((1,3),(5,11)))
if __name__=="__main__": main()
