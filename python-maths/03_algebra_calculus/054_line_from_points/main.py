def line_from_points(x1,y1,x2,y2):
    m=(y2-y1)/(x2-x1); c=y1-m*x1
    return m,c
def main():
    m,c=line_from_points(1,5,4,11)
    print(f"y = {m}x + {c}")
if __name__=="__main__": main()
