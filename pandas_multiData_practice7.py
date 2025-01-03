import pandas as pd
import matplotlib.pyplot as plt
from pandas.api.types import CategoricalDtype

# 그래프에 한글 나타내기 준비 
plt.rcParams['font.family'] = 'AppleGothic'
plt.rcParams['axes.unicode_minus'] = False

## (1) 데이터 준비 ------------------------------------
df = pd.read_csv('/Users/wooju-kang/Downloads/data/BostonHousing.csv')
df = df[['crim','rm','dis','tax','medv']]
df

titles = ['1인당 범죄율','방의 개수','직업센터까지의 거리','재산세','주택가격']

## (2) 그룹 칼럼 추가 ----------------------------------
grp = pd.Series(['M' for i in range(len(df))])
grp.loc[df.medv >= 25.0] = 'H'
grp.loc[df.medv >= 17.0] = 'L'
df['grp'] = grp


# 그룹 컬럼의 자료형과 레이블 순서 변경 
new_odr = ['H','M','L']
new_dtype = CategoricalDtype(categories=new_odr,ordered=True)
df.grp = df.grp.astype(new_dtype)
df.grp.dtype

df.shape
df.head()      
df.dtypes                                                                # 컬럼별 자료형 
df.grp.value_counts(sort = False)                                        # 주택가격 그룹별 분포


## (4) 히스토그램 --------------------------------------

# 화면 분할 정의 
fig,axes = plt.subplots(nrows=2,ncols=2)
fig.subplots_adjust(hspace=0.5,wspace=0.3)                               # 그래프 여백 

# 각 분할 영역에 그래프 작성하기 
for i in range(5):
    df[df.columns[i]].plot.hist(ax=axes[i//3,i%3],
                               ylabel='',
                               xlabel=titles[i])
    
# 통합 그래프에 제목 지정 
fig.suptitle('Histogram',fontsize=14)

# 분할 그래프 화면에 나타내기 
fig.show()


## (5) 상자그림 ---------------------------------------

fig,axes = plt.subplots(nrows=2,ncols=3)
fig.subplots_adjust(hspace=0.5,wspace=0.3)                                # 그래프 여백 

# 각 분할 영역에 그래프 작성하기 
for i in range(5):
    df[df.columns[i]].plot.box(ax=axes[i//3,i%3],
                               label=titles[i])
    
fig.suptitle('Boxplot',fontsize=14)
fig.show()


## (6) 그룹별 상자그림 ----------------------------------

fig,axes = plt.subplots(nrows=2,ncols=3)
fig.subplots_adjust(hspace=0.5,wspace=0.3)                                 # 그래프 여백 

# 각 분할 영역에 그래프 작성하기 
for i in range(5):
    df.boxplot(column=df.columns[i],
               by='grp',
               grid=False,
               ax=axes[i//3,i%3],
               xlabel=titles[i])
    

fig.suptitle('Boxplot by group',fontsize=14)
fig.show()

## (7) 산점도 -----------------------------------------
pd.plotting.scatter_matrix(df.iloc[:,:5])
plt.show()


## (8) 그룹이 있는 산점도 --------------------------------
dict = {'H':'red','M':'green','L':'gray'}
colors = list(dict[key] for key in df.grp)

pd.plotting.scatter_matrix(df.iloc[:,:5],c=colors)
plt.show()

## (9) 상관계수 ----------------------------------------
df.iloc[:,:5].corr()
