import pandas as pd

df = pd.read_csv('/Users/wooju-kang/Downloads/data/iris.csv') 

# 동률인 등수에 대해서는 평균으로 계산한다. 
# 순위 
df['Petal_Length'].rank().astype(int)                                # 오름차순 순위  
df['Petal_Length'].rank(ascending=False).astype(int)                 # 내림차순 순위  
