# 여러 변수들간의 산점도

import pandas as pd
import matplotlib.pyplot as plt

# 데이터 읽기
df = pd.read_csv('/Users/wooju-kang/Downloads/data/mtcars.csv')


# 다중 산점도의 작성
vars = ['mpg','disp','drat','wt']
pd.plotting.scatter_matrix(df[vars])
plt.show()