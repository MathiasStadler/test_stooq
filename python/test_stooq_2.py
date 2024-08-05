import pandas_datareader as pdr
dfr = pdr.stooq.StooqDailyReader(
# symbols=[ 'META.US', 'MSFT.US', 'GOOG.US'],
symbols=[ 'TREX.US'],
start='1/1/1990',
end='31/12/24'
)
df = dfr.read()
print(df.head())


# for debian 12
# sudo apt update
# sudo apt install python3 python3-dev virtualenv cmake libxml2 libxslt-dev

# virtualenv my_project_env
# source my_project_env/bin/activate
# pip install --upgrade pip

# check yor inside env
# pip install --upgrade setuptools wheel
# pip install pandas_datareader

# cd python
# python3 test_stooq_2.py