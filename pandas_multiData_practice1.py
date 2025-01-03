# 산점도 

import pandas as pd 
import matplotlib.pyplot as plt 

# 데이터 읽기 
df = pd.read_csv('/Users/wooju-kang/Downloads/data/mtcars.csv')
df

# 기본 산점도 
df.plot.scatter(x='wt',y='mpg')
plt.show()

# 매개변수 조정 산점도 
df.plot.scatter(x='wt',                  # x축의 변수명 
                y='mpg',                 # y축의 변수명  
                s=50,                    # 점의 크기  
                c='red',                 # 점의 색깔  
                marker='s')              # 점의 모양 
plt.show()