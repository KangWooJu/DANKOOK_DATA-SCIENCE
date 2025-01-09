import pandas as pd

df1=pd.DataFrame([['a',90],
                  ['b',80],
                  ['c',40]],
                  columns=['name','kor'])

df2=pd.DataFrame([['a',75],
                  ['b',60],
                  ['d',90]],
                 columns=['name','math'])

df1
df2

df12 = df1.merge(df2,on='name')                   # inner : 두 데이터프레임의 공통 칼럼의 값이 일치하는 행들끼리 연결하여 병합 
df12

df12 = df1.merge(df2,how='left',on='name')        # left : 왼쪽에 있는 데이터프레임을 기준으로 공통 칼럼의 값이 일치하는 행들끼리 연결하여 병합 
df12

df12 = df1.merge(df2,how='right',on='name')       # right : 오른쪽에 있는 데이터프레임을 기준으로 공통 컬럼의 값이 일치하는 행들끼리 연결하여 병합  
df12

df12 = df1.merge(df2,how='outer',on='name')       # outer : 'left'의 결과와 'right'의 결과의 합집합 
df12