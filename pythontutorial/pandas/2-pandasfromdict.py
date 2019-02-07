#https://pythonprogramming.net

import pandas as pd

web_stats = {'Day':[1,2,3,4,5,6],
             'Visitors':[43,34,65,56,29,76],
             'Bounce Rate':[65,67,78,65,45,52]}

df = pd.DataFrame(web_stats)

print(df.head())
print(df.tail())
print(df.head(2))
print(df.tail(2))

df.set_index('Day', inplace=True)
print(df.head())

df['Visitors'].plot()
plt.show()

df.plot()
plt.show()

print(df[['Visitors','Bounce Rate']])
