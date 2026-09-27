tp,fp,tn,fn=8,2,9,1
precision=tp/(tp+fp); recall=tp/(tp+fn)
specificity=tn/(tn+fp); accuracy=(tp+tn)/(tp+fp+tn+fn)
print("precision",precision,"recall",recall,"specificity",specificity,"accuracy",accuracy)
