import pandas as pd

score = pd.Series([30,20,40,pd.NA,30,pd.NA])
score
score.sum()                                               # 결측값을 제외하고 계산 
score.mean()                                              # 결측값을 계산하고 계산 
score + 5                                                 # 결측값은 산술 연산 안됨 

pd.isna(score)                                            # 결측값인지 여부 확인 
pd.isna(score).sum()                                      # 결측값의 개수 확인 

score.size()                                              # 값의 개수 (결측값 포함)
score.count()                                             # 값의 개수 (결측값 제외)

pd.notna(score)                                           # 결측값이 아닌지 여부 확인  
pd.notna(score).sum()                                     # 결측값이 아닌 값의 개수 확인  

score = score.dropna()                                    # 결측값을 제거  
score 
score = score.reset_index(drop=True)                       # 인덱스 초기화 
score 