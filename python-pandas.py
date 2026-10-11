import numpy as np
import pandas as pd


data_series = np.random.normal(0, 1, 100)


p_series = pd.Series(data_series)

print(p_series.head())
print(p_series.tail())



data_series2 = np.random.normal(0, 1, 100)


frame = {
    'column1': data_series,
    'column2': data_series2
}


df = pd.DataFrame(frame)


print(df)

print(df.describe())
print(df.sort_values(by='column1'))
df['Total'] = df['column1'] + df['column2']
print(df)

df.drop(columns='Total', inplace=True)
print(df)