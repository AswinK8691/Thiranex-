import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

df=pd.read_excel('Customer_Segmentation_Dataset.xlsx')
X=df[['AnnualIncome','SpendingScore']]
X=StandardScaler().fit_transform(X)
kmeans=KMeans(n_clusters=4,random_state=42,n_init=10)
df['Cluster']=kmeans.fit_predict(X)
print(df.head())

plt.scatter(df['AnnualIncome'],df['SpendingScore'],c=df['Cluster'])
plt.xlabel('Annual Income')
plt.ylabel('Spending Score')
plt.title('Customer Segments')
plt.show()
