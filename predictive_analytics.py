import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import numpy as np

df=pd.read_excel('Predictive_Analytics_Dataset.xlsx')
df['MonthNo']=range(1,13)
X=df[['MonthNo']]
y=df['Sales']
model=LinearRegression()
model.fit(X,y)
future=pd.DataFrame({'MonthNo':[13,14,15]})
pred=model.predict(future)
print(pred)
plt.plot(df['MonthNo'],y,label='Historical')
plt.plot(future['MonthNo'],pred,label='Forecast')
plt.legend()
plt.show()
