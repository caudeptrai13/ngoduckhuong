import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("Car_sales.csv")
print(df.head(20))
print(df.groupby(['Manufacturer'])['Sales_in_thousands'].sum()) #Cach 1
sale = df.pivot(columns='Manufacturer',values='Sales_in_thousands') #Cach 2
print("----------------------------------------------")
print(sale.sum(axis=0,skipna=True))
print("----------------------------------------------")
print(df[['Manufacturer','Sales_in_thousands']].groupby(['Manufacturer']).sum()) #Cach 3
df[df['Manufacturer'] == 'Chevrolet'][['Model','Power_perf_factor']].set_index('Model').plot()
plt.show()