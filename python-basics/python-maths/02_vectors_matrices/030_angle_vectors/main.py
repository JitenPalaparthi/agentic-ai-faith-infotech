import numpy as np
def angle_degrees(a,b):
    cosine=(a@b)/(np.linalg.norm(a)*np.linalg.norm(b))
    return np.degrees(np.arccos(np.clip(cosine,-1,1)))
def main():
    a=np.array([1.,0.]); b=np.array([1.,1.])
    print("Angle:",angle_degrees(a,b),"degrees")
if __name__=="__main__": main()
