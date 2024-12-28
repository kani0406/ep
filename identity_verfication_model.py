from sklearn.ensemble import IsolationForest
import pandas as pd


data = pd.read_csv('identity_data.csv')  
X = data[['feature1', 'feature2']]  


model = IsolationForest()
model.fit(X)


data['anomaly'] = model.predict(X)
print(data[data['anomaly'] == -1]) 
