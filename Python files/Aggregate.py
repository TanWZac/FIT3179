from os import rename
import pandas as pd

url = 'https://raw.githubusercontent.com/WenTanZac0625/FIT3179/main/data/vaccination_data.csv'
df = pd.read_csv(url, index_col=0)

lst = []
def total(col):
    p = df[col].sum()
    lst.append((col, p))

for i in range(12, 27):
    colname = df.columns[i]
    total(colname)

d = pd.DataFrame.from_records(lst,columns = ["Vaccine", "Each Country Usage"])
d.to_csv("Vaccine_used.csv")