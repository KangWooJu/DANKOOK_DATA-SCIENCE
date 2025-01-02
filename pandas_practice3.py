import pandas as pd


# 판다스의 DataFrame에서 레이블 지정하기 
score = pd.DataFrame([[85,96,40,95],
                      [73,69,45,80],
                      [78,50,60,90]])

score
score.index = ['John','Jane','Tom']
score.columns = ['KOR','ENG','MATH','SCI']
score

score.iloc[2,1]
score.loc['Tom',"ENG"] 