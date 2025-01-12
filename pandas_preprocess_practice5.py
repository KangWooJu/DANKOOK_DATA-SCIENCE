import pandas as pd

df = pd.read_csv('/Users/wooju-kang/Downloads/data/iris.csv') 

# 데이터프레임의 정렬 
# 오름차순 정렬 
df_sorted = df.sort_values('Sepal_Length')
df_sorted.head(10)


# 내림차순 정렬 
df_sorted = df.sort_values('Sepal_Length',ascending=False)
df_sorted.head(10)


# 여러 개의 기준 컬럼을 적용 
df_sorted = df.sort_values(['Species','Sepal_Width'])                 # 1차로는 Species 컬럼을 기준으로 값이 동일한 행 , 2차로는 Sepal_Width 컬럼의 값을 기준으로 오름차순 정렬 
df_sorted.head(10)

