# import pandas_datareader as pdr
from pandas_datareader import data as pdr
# dfr = pdr.stooq.StooqDailyReader(
#     # symbols=[ 'META.US', 'MSFT.US', 'GOOG.US'],
#     symbols=['TREX.US'],
#     start='1/1/24',
#     end='12/24/24'
# )
# df = dfr.read()
# print(df.head())

symbols = ['TREX.US']
for i in symbols:
    pdr.DataReader(i,'yahoo','2024-01-01','2024-12-31').to_csv(i+'.csv')




# for start
# virtualenv my_project_env
# source my_project_env/bin/activate
# python3 test_stooq_2.py

# Save an object from pandas_datareader into a csv file in Python 3.5
# https://stackoverflow.com/questions/41962745/save-an-object-from-pandas-datareader-into-a-csv-file-in-python-3-5
