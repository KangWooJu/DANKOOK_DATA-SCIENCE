# 복수의 선 그래프 생성

import pandas as pd 
import matplotlib.pyplot as plt 

late1=[5,8,7,9,4,6,12,13,8,6,6,4]
late2=[4,6,5,8,7,8,10,11,6,5,7,3]

dict = {'class_1':late1,'class_2':late2}
late = pd.DataFrame(dict,
                    index=list(range(1,13)))
late

late.plot(title='Late Student per month',      
          xlabel='month',
          ylabel='frequency',
          marker='o')
plt.legend(loc='upper right')                    # 범례지정 
plt.show()