import pandas_datareader as pdr
dfr = pdr.stooq.StooqDailyReader(
symbols=[ 'META.US', 'MSFT.US', 'GOOG.US'],
start='1/1/24',
end='3/8/24'
)
df = dfr.read()
print(df.head())


# virtualenv my_project_env
# source my_project_env/bin/activate


# sudo apt install python3 python3-dev