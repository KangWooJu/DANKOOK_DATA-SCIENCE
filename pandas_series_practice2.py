# 3주차 - 판다스 시리즈 객체 (2)

import pandas as pd

salary = pd.Series([20,15,18,30])                           # 레이블 인덱스가 없는 시리즈 객체 
score = pd.Series([75,80,90,60],
                  index=['KOR','ENG','MATH','SOC'])        

salary
score

# 값의 변경 
score.iloc[0] = 85                                          # 인덱스 0 의 값을 변경
score
score.loc['SOC'] = 65                                       # 인덱스 'SOC' 의 값을 변경 
score
score.loc[['ENG','MATH']] = [70,80]                         # 인덱스 'ENG','MATH' 의 값을 변경 
score

# 값의 추가 ( 레이블 인덱스가 있는 경우 )
score.loc['PHY'] = 50                                       # 없는 인덱스 추가 
score
score.iloc[5] = 90                                          # 에러 발생 


# 값의 추가 ( 레이블 인덱스가 없는 경우 )
next_idx = salary.size
salary.iloc[next_idx] = 33                                  # 에러 발생 
salary.loc[next_idx] = 33                                   # 정상 수행 
salary

# _append() 메서드를 이용한 값의 추가 
new = pd.Series({'MUS':95})                                 
score._append(new)                                          # score 변경 없음 
score
score = score._append(new)                                  # score 변경됨 
score

# 레이블을 지정하지 않은 시리즈 객체의 경우 새로운 값을 추가하는 예 
salary = salary._append(pd.Series([66]),ignore_index=True)
salary

# 값의 삭제 
salary = pd.Series([20,15,18,30,10])
score = pd.Series([75,80,90,60,10],
                  index=['KOR','ENG','MATH','SOC','PHY'])

score.drop('PHY')                                           # 레이블 인덱스가 있는 경우 
score                                                       # score의 내용 변동 없음 

score = score.drop('PHY')
score                                                       # score의 내용 변경 

salary = salary.drop(1)                                     # 레이블 인덱스가 없는 경우 
salary
