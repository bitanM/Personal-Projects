import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
%matplotlib inline
ds = pd.read_csv("/content/zomato.csv", encoding='latin-1')
ds.head()
ds.columns
ds.info()
ds.describe()
ds.isnull().sum()
[features for features in ds.columns if ds[features].isnull().sum()>0]
sns.heatmap(ds.isnull(), yticklabels=False, cbar=False, cmap='viridis')
country = pd.read_excel("/content/Country-Code.xlsx")
country.head()
final = pd.merge(ds, country, on="Country Code", how='left')
country
final.head(10)
country_name = final.Country.value_counts().index
country_value = final.Country.value_counts().values
plt.pie(country_value[:4],labels=country_name[:4], autopct='%1.4f%%')
ratings = final.groupby(['Aggregate rating', 'Rating color', 'Rating text']).size().reset_index().rename(columns={0:'Rate Count'})
print(ratings)
sns.barplot(x='Aggregate rating', y='Rating text', data = ratings)
plt.rcParams['figure.figsize']=(12,6)
sns.barplot(x='Aggregate rating', y='Rate Count',hue='Rating color', data=ratings)
sns.countplot(x='Rating color', data=ratings)
final[final['Aggregate rating']==4.5].groupby('Country').size().reset_index()
final
final[final['Aggregate rating']==4.5].groupby('Restaurant Name').size().reset_index()
final[['Country','Currency']].groupby(['Country','Currency']).size().reset_index()
final[['Has Online delivery','Country']].groupby(['Has Online delivery','Country']).size().reset_index()
plt.pie(final.Country.value_counts().values[:4],labels=final.City.value_counts().index[:4], autopct='%1.4f%%')
