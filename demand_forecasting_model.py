import pandas as pd
from statsmodels.tsa.arima.model import ARIMA


data = pd.read_csv('sales_data.csv')  
data['date'] = pd.to_datetime(data['date'])
data.set_index('date', inplace=True)


model = ARIMA(data['sales'], order=(5, 1, 0))  
model_fit = model.fit()


forecast = model_fit.forecast(steps=10) 
print(forecast)
