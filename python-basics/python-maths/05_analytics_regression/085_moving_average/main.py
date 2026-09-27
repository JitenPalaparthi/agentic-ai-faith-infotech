import pandas as pd
def main():
    s=pd.Series([10,12,11,15,18,17,20],name="value")
    print(pd.DataFrame({"value":s,"MA3":s.rolling(3).mean()}))
if __name__=="__main__": main()
