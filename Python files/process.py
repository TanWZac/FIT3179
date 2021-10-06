from os import rename
import pandas as pd
from pandas.core.indexes.api import all_indexes_same

url = 'https://raw.githubusercontent.com/WenTanZac0625/FIT3179/main/data/vaccination_data.csv'
df = pd.read_csv(url, index_col=0)
data = pd.DataFrame(df.groupby('WHO_REGION').agg({'Pfizer BioNTech - Comirnaty':['sum']}))

def ag(col, data):
    c = df.groupby('WHO_REGION').agg({col:['sum']})
    data = pd.concat([data, c], axis=1)
    return data

for i in range(13, 27):
    colname = df.columns[i]
    data = ag(colname, data)

data = data.T
data.to_csv("Vaccine_used.csv")