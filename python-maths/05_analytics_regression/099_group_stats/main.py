import pandas as pd
def main():
    df=pd.DataFrame({"team":["A","A","A","B","B"],"score":[10,20,30,25,45]})
    print(df.groupby("team")["score"].agg(["count","mean","median","std"]))
if __name__=="__main__": main()
