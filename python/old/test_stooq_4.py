import pandas_datareader as pdr
dfr = pdr.stooq.StooqDailyReader(
symbols=[ 'TREX.US'],
start='1/1/24',
end='3/8/24'
)

# FROM HERE
# https://github.com/pydata/pandas-datareader/issues/925
# StooqDailyReader('^DJI').read().sort_index(ascending=True)

df = dfr.read().sort_index(ascending=True)
print(df.head())
