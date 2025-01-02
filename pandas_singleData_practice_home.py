import pandas as pd 
import matplotlib.pyplot as plt 
import numpy as np


df = pd.read_csv('/Users/wooju-kang/Downloads/data/user_behavior_dataset.csv')

models = df['Device_Model']                                                           # 스마트폰 모델 정보 ( 범주형 자료 )
usage_time = df['App_Usage_Time']                                                     # 앱사용 시간 ( 연속형 자료 ) 

# 문제 1
models.value_counts()

# 문제 2
models.value_counts()/models.size

# 문제 3 
models.value_counts().plot.bar(xlabel='Device_Model',
                      ylabel='Count',
                      rot=0,
                      title='SmartPhone Usage')
plt.show()

models.value_counts().plot.pie(ylabel='',
                autopct='%1.0f%%',
                title='SmartPhone Usage')
plt.show()

# 문제 4 
usage_time.mean()
usage_time.median()
usage_time.quantile([0.25,0.5,0.75])
usage_time.var()
usage_time.std()

# 문제 5
usage_time.hist(bins=6)
plt.show()

# 문제 6
usage_time.plot.box(title='Usage Time')
plt.show()

# 문제 7
df.boxplot(column='App_Usage_Time',
                    by='Operating_System',
                    grid=False)
plt.suptitle('')
plt.show()

# 문제 8

fig,axes = plt.subplots(nrows=2,ncols=2)

usage_time.plot.hist(ax=axes[0,0])
usage_time.plot.box(ax=axes[0,1])

fig.suptitle("5,6 Graph")
plt.show()