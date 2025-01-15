# 윌콕슨 부호 순위 검정 

import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt

df = pd.read_csv('/Users/wooju-kang/Downloads/data/wilcoxon_test.csv')
df 

# 데이터 탐색 
df.mean()                                                                 # 그룹별 평균 
(df['post']-df['pre']).mean()                                             # pre , post 차이의 평균     

fig,axes = plt.subplots(nrows=1,ncols=2)
df['pre'].plot.box(grid=False,ax=axes[0])
plt.ylim([60,100])
df['post'].plot.box(grid=False,ax=axes[1])
plt.show() 


# 윌 콕슨 부호순위 검정 
stats.wilcoxon(df['pre'],df['post'])                                      # p - value 가 유의 수준인 0.05 보다 큰 경우 귀무가설을 기각할 수 없다. 


