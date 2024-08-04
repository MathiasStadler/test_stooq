# FROM HERE
# file:///home/trapapa/Downloads/pandas-datareader-readthedocs-io-en-latest.pdf

from pandas_datareader.nasdaq_trader import get_nasdaq_symbols
from pathlib import Path


filepath = Path('output/out.csv')

filepath.parent.mkdir(parents=True, exist_ok=True)


df = get_nasdaq_symbols()
print(df.loc['IBM'])
# df.to_csv('nasdaq_trader.csv')
