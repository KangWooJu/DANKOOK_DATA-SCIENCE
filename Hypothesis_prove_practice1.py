# 샤피로 검정 

import pandas as pd
from scipy import stats 
import matplotlib.pyplot as plt 

df = pd.read_csv('/Users/wooju-kang/Downloads/data/ind_ttest.csv')

# 데이터 탐색
df.head()
df.groupby('group').count()                                       # 그룹별 표본 크기 
df.groupby('group').mean()                                        # 그룹별 평균  
df.groupby('group').boxplot(grid=False)                           # 그룹별 plotbox 생성 -> 각 그룹별 비교를 위함 
plt.show() 

group_1 = df.loc[df.group == 'A','height']
group_2 = df.loc[df.group=='B','height']
group_1
group_2

# 정규성 검정 
stats.shapiro(group_1)                                             # 샤피로 검정을 사용 
stats.shapiro(group_2)

# 등분산성 검정
stats.levene(group_1,group_2)                                      # 귀무가설 ( : 대상 표본은 정규성을 만족한다. ) 를 채택 

# 독립표본 T - 검정
result = stats.ttest_ind(group_1,group_2,equal_var=True)
result 

