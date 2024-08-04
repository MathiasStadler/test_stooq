# FROM HERE
# https://pandas-datareader.readthedocs.io/en/latest/remote_data.html

import pandas_datareader.data as web
f = web.DataReader('^DJI', 'stooq')

print(f.head())