import pandas as pd


age = pd.Series([25,34,19,45,60])
age.index = ['John','Jane','Tom','Micle','Tom']
age

age.iloc[3]
age.loc['Tom']
# 레이블의 중복 가능성 