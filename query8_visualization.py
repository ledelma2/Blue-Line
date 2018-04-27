#from pandas import DataFrame, read_csv
#import matplotlib.pyplot as plt
import pandas as pd


# file = r'query8.csv'

df = pd.read_csv('query8.csv', encoding="utf-8")
col1 = df['Name']
col2 = df['Address']
col3 = df['Failed inspection on']
col4 = df['Alive for x years']




