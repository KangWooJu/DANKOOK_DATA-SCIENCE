# 한 화면에 여러개의 그래프를 출력하기 

import pandas as pd
import matplotlib.pyplot as plt

# 데이터 읽기 
df = pd.read_csv('/Users/wooju-kang/Downloads/data/iris.csv')

# 화면 분할 정의 
fig,axes = plt.subplots(nrows=2,ncols=2)

# 각