# 대응표본 T-검정

import pandas as pd
from scipy import stats 
import matplotlib.pyplot as plt 

df = pd.read_csv('/Users/wooju-kang/Downloads/data/paired_ttest.csv')


# 데이터 탐색 

df.head()
df[['before','after']].mean()                                        # 그룹별 평균  
(df['after']-df['before']).mean()                                    # before , after 차이의 평균 

fig,axes = plt.subplots(nrows=1,ncols=1)
df['before'].plot.box(grid=False,
                      ax = axes[0])
plt.ylim([60,100])                                                   # y - label의 값을 60 ~ 100 사이로 조정  
df['after'].plot.box(grid=False,
                     ax=axes[1])
plt.show()


# 정규성 검정 
stats.shapiro(df['after']-df['before'])


# 대응 표본 T - 검정 
result = stats.ttest_rel(df['before'],df['after'])
result                                                                # 대응표본 T - 검정의 실시결과인 p - value의 값이 0.05보다 큰 경우 대립가설을 채택할 수 없다.  
