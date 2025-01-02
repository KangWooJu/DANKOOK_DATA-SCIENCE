import pandas as pd
import matplotlib.pyplot as plt 

# 데이터 준비 
df = pd.read_csv('/Users/wooju-kang/Downloads/data/cars.csv')
dist = df['dist']                                                    # 제동거리 


# 상자그림 그리기
dist.plot.box(title='Breaking distance')
plt.show()

