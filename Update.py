import numpy as np
import pandas as pd
from pandas.core.frame import DataFrame
import requests
from io import StringIO

url = 'https://raw.githubusercontent.com/govex/COVID-19/master/data_tables/vaccine_data/global_data/vaccine_data_global.csv'
url = "https://github.com/govex/COVID-19/blob/master/data_tables/vaccine_data/global_data/vaccine_data_global.csv"
resp = requests.get(url)

data = pd.read_csv("https://covid19.who.int/who-data/vaccination-data.csv")
result = pd.concat([data['COUNTRY'], data['TOTAL_VACCINATIONS']], axis= 1)
result.reset_index(drop = True, inplace = True)
print(result)
# result.to_csv("Total_vaccination.csv")