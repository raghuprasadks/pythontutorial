# -*- coding: utf-8 -*-
import pandas as pd
import datetime
import pandas_datareader.data as web
import matplotlib.pyplot as plt
from matplotlib import style
from pandas_datareader.quandl import QuandlReader 

style.use('fivethirtyeight')

START = datetime.datetime(2010,1,1)
END = datetime.datetime.now()
ticker='XOM'

#df=web.DataReader("XOM","morningstar",start,end)



data = QuandlReader("WIKI/{}".format(ticker), start=START, end=END) 
df = data.read()
print(df)
print(df.head())

df['High'].plot()
plt.legend()
plt.show()

print(web.get_data_fred('GS10'))

