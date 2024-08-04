import pandas_datareader as pdr

from pathlib import Path  
import pandas_datareader.data as web

filepath = Path('output/trex.csv')  

filepath.parent.mkdir(parents=True, exist_ok=True) 

dfr = pdr.stooq.StooqDailyReader(
symbols=[ 'TREX.US'],
start='1/1/14',
end='3/8/24'
)

# FROM HERE
# https://github.com/pydata/pandas-datareader/issues/925
# StooqDailyReader('^DJI').read().sort_index(ascending=True)

df = dfr.read().sort_index(ascending=True)
df.to_csv(filepath)
print(df.head())
