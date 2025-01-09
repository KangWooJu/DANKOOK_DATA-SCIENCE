# 그래프에 한글 표시하기 

import pandas as pd 
import matplotlib.pyplot as plt

plt.rcParams['font.family'] = 'AppleGothic'            # 한글 폰트 변경  
plt.rcParams['axex.unicode_minus'] = False               # 마이너스부호 깨짐 방지 


ser = pd.Series([1,2,3,3])
ser.plot.hist(title=' 그래프 예제 - 히스토그램')
plt.show()