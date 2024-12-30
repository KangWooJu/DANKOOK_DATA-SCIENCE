import pandas as pd

# 문제 1번 
sales = pd.Series([781,650,705,406,580,450,550,640],
                  index=['A','B','C','D','E','F','G','H'])

sales

# 문제 2번 
len(sales)

# 문제 3번
sales.iloc[1]

# 문제 4번
sales.loc['F']

# 문제 5번 
sales.iloc[3:6]

# 문제 6번
sales.loc[['A','B','C']]

# 문제 7번
sales.loc[(sales<500)|(sales>700)]

# 문제 8번
team_B = sales.loc['B']
sales.loc[sales>team_B]

# 문제 9번
sales.loc[sales<600].index

# 문제 10번 
under_600 = sales.loc[sales<600]
under_600 * 120 / 100

# 문제 11번 
sales.mean()
sales.sum()
sales.std()

# 문제 12번 
sales.loc['A'] = 810
sales.loc['C'] = 820
sales

# 문제 13번
new = pd.Series({'J':400})
sales._append(new)

# 문제 14번 
sales.drop('J')
sales

# 문제 15번 
sales2 = sales.copy()
sales2 + 500

sales
sales2