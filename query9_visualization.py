from pandas import DataFrame, read_csv
import matplotlib.pyplot as plt
import pandas as pd


# file = r'query8.csv'

df = pd.read_csv('query9.csv', encoding="utf-8")
col1 = df['Census Block']
col2 = df[' # of Businesses with liquor licenses']
col3 = df[' # of Crimes']
col4 = df[' # of Arrests']
df.head(2);

df.plot.scatter(col2, col4)

dataframe = pd.DataFrame({'Col': np.random.uniform(size=1000)})
plt.scatter(dataframe.index, dataframe['Col'])


