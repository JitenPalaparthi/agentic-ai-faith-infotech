import pickle, numpy as np
with open('../linear_regression_model.pkl','rb') as f: model=pickle.load(f)
# area_sqft, bedrooms, age_years, distance_city_km
x=np.array([[1800,3,5,8]],dtype=np.float32)
print('Predicted price (lakhs):', float(model.predict(x)[0]))
