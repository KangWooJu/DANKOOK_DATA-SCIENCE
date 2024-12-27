import pandas as pd

# 판다스의 DataFrame Set 사용하기 
score = pd.DataFrame([[85,96,40,95],
                      [73,69,45,80],
                      [78,50,60,90]])

score
type(score)

score.index
score.columns

score.iloc[1,2]