# 맨 휘트니 검정 

import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt

df = pd.read_csv('/Users/wooju-kang/Downloads/data/mw_test.csv')


# 데이터 탐색 
df.head()
df.groupby('group').count()                                    # 그룹별 표본 크기 
df.groupby('group').mean()                                     # 그룹별 평균 
df.groupby('group').boxplot(grid=False)
plt.show() 

group_1 = df.loc[df.group=='A','score']
group_2 = df.loc[df.group=='B','score']


# 맨 휘트니 검정 
stats.mannwhitneyu(group_1,group_2)                             # p - value가 유의수준보다 높은 경우 두 그룹의 평균은 유의미한 차이가 없다고 판단한다. 