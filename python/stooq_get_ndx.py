# FROM HERE
# https://pandas-datareader.readthedocs.io/en/latest/remote_data.html

# to_csv
# https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_csv.html

from pathlib import Path  
import pandas_datareader.data as web

filepath = Path('output/dji.csv')  

filepath.parent.mkdir(parents=True, exist_ok=True)  

# df.to_csv(filepath)

df = web.DataReader('^NDX', 'trex')
df.to_csv(filepath)

print(df.head())