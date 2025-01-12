import pandas as pd 
df = pd.read_csv('/Users/wooju-kang/Downloads/data/iris.csv') 


# 데이터 집계 

df_agg = df.groupby('Speices').mean()
df_agg = df.groupby('Species').std()

df_agg = df.groupby(['cyl','vs']).max()
df_agg 
