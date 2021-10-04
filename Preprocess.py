from os import rename
import pandas as pd

url = 'https://raw.githubusercontent.com/WenTanZac0625/FIT3179/main/data/vaccination_data.csv'
df = pd.read_csv(url, index_col=0)
data = pd.DataFrame(df.groupby('WHO_REGION').agg({'PERSONS_VACCINATED_1PLUS_DOSE_PER100':['sum']}))
data1 = df.groupby('WHO_REGION').agg({'PERSONS_FULLY_VACCINATED_PER100':['sum']})
cont = pd.concat([data, data1], axis =1 )
cont.to_csv("Total_vaccination_per_region.csv")