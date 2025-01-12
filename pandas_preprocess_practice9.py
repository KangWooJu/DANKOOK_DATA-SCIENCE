import pandas as pd
df = pd.read_csv('/Users/wooju-kang/Downloads/data/mtcars.csv')


df_agg = df.groupby(['cyl','vs']).max()
df_agg 