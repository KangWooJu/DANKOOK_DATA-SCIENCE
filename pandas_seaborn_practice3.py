import seaborn as sns 
import matplotlib.pyplot as plt 
import pandas as pd 

df=pd.read_csv('/Users/wooju-kang/Downloads/data/seoul_temp.csv')
df.head()
df['month']=(df.날짜 - 2023000) // 100             # ' 월 ' 컬럼 생성   
df.head()

# 그래프 테마 설정 
sns.set_theme(style="white",rc={"figure.figsize":(7,4)})

# 월별 평균 기온에 의한 순위 계산 
tmp = df.groupby('month').mean()
rank = tmp['평균기온'].rank() - 1
rank = rank.astype(int).to_list()


# 팔레트 색 선택및 순서 변경 
mycolor = sns.color_palette('bwr',12)
mycolor = pd.Series(mycolor)[rank].to_list()

# 월별 기온 분포를 상자그림으로 작성
plt.rcParams['font.family'] = 'AppleGothic'
plt.rcParams['axes.unicode_minus'] = False

sns.boxplot(data=df,
            x='month',
            y='평균기온',
            hue='month',
            legend=None,                              # 범례 표시 X
            palette=mycolor                            # 팔레트 지정  
            ).set(title='월별 기온 분포')

plt.ylabel('기온')
plt.subplots_adjust(bottom=0.2)
plt.show()