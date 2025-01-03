# 상관분석의 계산 

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

beers = [5,2,9,8,3,7,3,5,3,5]                                    # 음주량  
bal = [0.1,0.03,0.19,0.12,0.04,0.0095,0.07,                      # 혈중알콜 농도  
       0.06,0.02,0.05]

dict = {'beers':beers,'bal':bal}                                 # 딕셔너리 정의  
df = pd.DataFrame(dict)                                          # 데이터프레임 생성  
df
df.plot.scatter(x='beers',y='bal',                               # 산점도  
                title='Beers~Blood Alcohol Level')


# 회귀식 계산 

m,b = np.polyfit(beers,bal,1)

# 회귀선 출력

plt.plot(beers,m*np.array(beers)+b)
plt.show()


# 두 변수간 상관계수 계산
df['beers'].corr(df['bal'])

# 여러 변수들간 상관계수
df2 = pd.read_csv('/Users/wooju-kang/Downloads/data/iris.csv')    # csv 파일 입력 
df2.columns                  
df2 = df2.loc[:,~df2.columns.isin(['Species'])]                   # Species 컬럼 제외하기  
df2.columns

df2.corr()                                                        # 상관계수 계산 
df2.corr(method='pearson')                                        # 피어슨 상관 계수 ( 기본 )
df2.corr(method='kendall')                                        # 켄달 - 타우 상관 계수
df2.corr(method='spearman')                                       # 스피어맨 상관 계수 

