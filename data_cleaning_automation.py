import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_excel('Data_Cleaning_Automation_Dataset.xlsx')

df=df.drop_duplicates()
df['Age']=df['Age'].fillna(df['Age'].median())
df['City']=df['City'].fillna('Unknown')
df['Sales']=df['Sales'].fillna(df['Sales'].mean())

summary=df.describe(include='all')
print(summary)

df.groupby('City')['Sales'].mean().plot(kind='bar')
plt.title('Average Sales by City')
plt.tight_layout()
plt.show()

summary.to_csv('cleaning_report.csv')
df.to_excel('cleaned_data.xlsx',index=False)
