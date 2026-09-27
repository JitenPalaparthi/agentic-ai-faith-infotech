import numpy as np
def main():
    x=np.array([10.,np.nan,30.,40.])
    print("Ordinary mean:",np.mean(x)); print("NaN-aware mean:",np.nanmean(x)); print("Median:",np.nanmedian(x))
if __name__=="__main__": main()
