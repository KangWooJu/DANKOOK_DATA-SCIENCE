import pandas as pd
import numpy as np

# 결측값을 포함하는 데이터프레임 생성 

df = pd.read_csv('/Users/wooju-kang/Downloads/data/iris.csv')
df.iloc[0,1] = pd.NA ; df.iloc[0,2] = pd.NA
df.iloc[1,2] = np.nan ; df.iloc[2,3] = None 
df.head() 

# 결측값의 확인  
df.isnull().sum()                                  # 컬럼별 결측값 확인 
df.isnull().sum(axis=1)                            # 행별 결측값 확인 
df.loc[df.isnull().sum(axis=1)>0,:]                # 결측값 행 출력  

# 결측값의 제거 
df = df.dropna()                                   # 결측값 포함행 제거  
df = df.reset_index(drop = True)                   # 인덱스 초기화  
df.head() 
      