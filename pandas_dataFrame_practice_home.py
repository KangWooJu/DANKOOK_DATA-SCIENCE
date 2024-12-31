import pandas as pd 

# 문제 1번 
dfs = pd.read_csv('/Users/wooju-kang/Downloads/data/GNI2014.csv')
dfs

dfs.head(5)

# 문제 2번  
dfs.shape[0]
dfs.shape[1]

# 문제 3번 
dfs['continent'] = dfs['continent'].astype('category') 
dfs['continent'].unique()

# 문제 4번
dfs.iloc[1,]

# 문제 5번 
dfs[dfs['continent']=='Europe']

# 문제 6번
dfs.loc[dfs.population >=50000000]

# 문제 7번 
result = dfs.loc[dfs['continent'] == 'Europe', 'population']
result
result.mean()

# 문제 8번 
result2 = dfs.loc[dfs['GNI'] >= 51630,'GNI']
result2.mean()

# 문제 9번 
dfs.loc['North Ameri']
northAmerica = dfs.loc[dfs['continent']=='North America','population']
(northAmerica*110)/100

# 문제 10번
europe_1_money = (dfs.loc[dfs['continent']=='Europe','GNI'] / dfs.loc[dfs['continent']=='Europe','population'])
europe_1_money

# 문제 11번 
PNP = europe_1_money.copy()
PNP.head(5)