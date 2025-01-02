import pandas as pd
import matplotlib.pyplot as plt

favorite = pd.Series(['WINTER','SUMMER','SPRING','SUMMER','SUMMER',       # 시리즈 객체 채우기
                      'FALL','FALL','SUMMER','SPRING','SPRING'])

favorite                                                                  # favorite 의 내용 출력하기  
favorite.value_counts()                                                   # 도수분포 계산 : 객체에 저장된 범주형 데이터에 대한 값을 종류별로 계산 
favorite.value_counts()/favorite.size                                     # 비율 계산  : 각 값의 종류별 비율을 계산 

fd = favorite.value_counts()                                              # 도수분포를 fd에 저장  
type(fd)                                                                  # fd의 자료구조 확인하기  
fd['SUMMER']                                                              # SUMMER 의 빈도 확인하기  
fd.iloc[2]                                                                # 인덱스 2번째의 빈도 확인하기 



fd.plot.bar(xlabel='Season',
            ylabel='Frequency',
            rot=0,
            title='Favorite Season')
plt.show()


# 막대그래프의 세로 출력 

fd.plot.barh(xlabel='Frequency',
             ylabel='Season',
             rot=0,
             title='Favorite Season')
plt.subplots_adjust(left=0.2)
plt.show

fd.plot.pie(ylabel='',
            autopct='%1.0f%%',
            title='Favorite Season')
plt.show()

