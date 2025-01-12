import pandas as pd
import numpy as np
from scipy import stats 

df = pd.read_csv('/Users/wooju-kang/Downloads/data/iris.csv')
sw = df.Sepal_Width 

# Z - score 이용 
z = np.abs(stats.zscore(sw))                                      # z - score의 절대값 구하기 
outliers = sw[z>2]                                                # z - score > 2를 만족하는 속성 분류 
print(outliers)

# IQR 이용
Q1 = sw.quantile(0.25)
Q3 = sw.quantile(0.75)
IQR = Q3 - Q1 

outliers = sw[(sw<Q1-IQR*1.5)|(sw>Q3+IQR*1.5)]                    # IQR*1.5 보다 큰 값 = 특이 값 
print(outliers)

# 특이값의 제거 
clean = sw.loc[~sw.isin(outliers)]
len(clean) 