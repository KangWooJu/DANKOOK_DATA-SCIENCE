import pandas as pd
import matplotlib.pyplot as plt

# 데이터 준비 
df = pd.read_csv('/Users/wooju-kang/Downloads/data/iris.csv')

# 상자그림 그리기
df.boxplot(column='Petal_Length',
           by='Species',
           grid=False)

plt.suptitle('')
plt.show()