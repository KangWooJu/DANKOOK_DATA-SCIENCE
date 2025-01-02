import pandas as pd
import matplotlib.pyplot as plt 

# 데이터 준비 
df = pd.read_csv('/Users/wooju-kang/Downloads/data/cars.csv')
dist = df['dist']
dist 


# 구간 개수를 지정하여 히스토그램 그리기 
dist.plot.hist()
plt.show()

dist.plot.hist(bins=6)                                              # 막대 개수 지정 
plt.show()

# 구간별 빈도수 계산 
dist.value_counts(bins=6,sort=False)

dist.plot.hist(bins=6,                                              # 막대 개수 지정 
               title='Braking distance',                            # 그래프 제목 
               xlabel='distance',                                   # x축 레이블  
               ylabel='frequency',                                  # y축 레이블  
               color='g')                                           # 막대색   
plt.show()