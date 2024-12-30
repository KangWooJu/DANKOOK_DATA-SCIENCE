# 3주차 - 판다스 시리즈 객체 (1)

import pandas as pd
import numpy as np

temp = pd.Series([-0.8,-0.1,7.7,13.8,18.0,22.4,
                  25.9,25.3,21.0,14.0,9.6,-1.4])

temp

temp.index
temp.index = ['1월','2월','3월','4월',
              '5월','6월','7월','8월','9월',
              '10월','11월','12월']
temp

temp.size                               # 배열의 크기 ( 값의 개수 )
len(temp)                               # 배열의 크기 ( 값의 개수 )
temp.shape                              # 배열의 형태 

temp.iloc[2]                            # 인덱스 2의 값
temp.loc['3월']                          # 인덱스'3월'의 값

temp.iloc[[3,5,7]]                      # 인덱스 3,5,7의 값
temp.loc[['4월','6월','8월']]             # 인덱스'4월','6월','8월'의 값

temp.iloc[5:8]                          # 인덱스 5~7의 값

temp.loc['6월':'9월']                    # 인덱스'6월'~'9월'의 값

temp.iloc[:4]                           # 인덱스 0~3의 값
temp.iloc[9:]                           # 인덱스 9~11의 값 
temp.iloc[:]                            # 인덱스 0~11의 값

temp.iloc[5:8]                          # 인덱스 5 ~ 7의 값 

temp.loc[temp >= 15]                    # 월평균 기온이 15도 이상인 월들의 기온 

temp.loc[(temp >= 15) & (temp < 25)]    # 월평균 기온이 15도 이상 25도 미만인 월들의 기온

temp.loc[(temp < 5) | (temp >= 25)]     # 월평균 기온이 5도 미만이거나 25도 이상인 월들의 기온 

# 3월보다 기온이 낮은 월들의 기온 
march = temp.loc['3월'] 
temp.loc[temp < march]

temp.where(temp >= 15)                  # where()를 이용한 조건 검색 
temp.where(temp >= 15).dropna()         # 결측값을 제외하고 조건에 맞는 값들만 보는 함수 

temp.loc[temp >= 15]                    # 조건에 맞는 값 추출 
temp.loc[temp >= 15].index              # 조건에 맞는 값들의 인덱스 추출 


# 시리즈 객체에 대한 산술 연산 
temp + 1    
2 * temp + 0.1
temp + temp
temp.loc[temp >= 15] + 1                # 기온이 15도 넘는 월들에 대해서만 1 증가        

temp.sum()                              # 값들의 합계

temp.mean()                             # 값들의 평균

temp.median()                           # 값들의 중앙값

temp.max()                              # 값들의 최대값

temp.min()                              # 값들의 최소값

temp.std()                              # 값들의 표준편차

temp.var()                              # 값들의 분산

temp.abs()                              # 값들의 절대값

temp.describe()                         # 기초통계정보                   

