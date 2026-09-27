b0,b_area,b_bed,b_age=20,.1,10,-.5
area,bedrooms,age=1000,3,10
price=b0+b_area*area+b_bed*bedrooms+b_age*age
print("prediction =",price)
