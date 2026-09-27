y=[1,0]; p=[.8,.3]
row_probs=[pi if yi==1 else 1-pi for yi,pi in zip(y,p)]
likelihood=1
for q in row_probs: likelihood*=q
print("row probabilities",row_probs,"likelihood",likelihood)
