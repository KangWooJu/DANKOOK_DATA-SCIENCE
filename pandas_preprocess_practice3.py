import pandas as pd
from sklearn.impute import KNNImputer

df_org = pd.read_csv('/Users/wooju-kang/Downloads/data/iris.csv')
df_miss = df_org.copy()

df_miss.iloc[0,3] = pd.NA ; df_miss.iloc[0,2] = pd.NA
df_miss.iloc[1,2] = None ; df_miss.iloc[2,3] = None 
df_miss.head(4)


# 결측값 추정  
tmp_np = df_miss.iloc[:,:4].to_numpy()                                # 넘파이 배열 변환  
imputer = KNNImputer(n_neighbors=5)                                   # 추정모델 정의   
tmp_np = imputer.fit_transform(tmp_np)                                # 결측값 추정  
df_miss.iloc[:,:4] = tmp_np                                           # 추정값 -> 결측값  


# 추정값의 정확도 확인 
df_miss.head(4)
df_org.head(4)