import seaborn as sns 
import matplotlib.pyplot as plt 

df = sns.load_dataset('flights')
df.head()

# 그래프 테마 설정 
sns.set_theme(style="whitegrid",
              rc={"figure.figsize":(8,5)})             # 그래프의 크기를 가로:8 , 세로:5로 지정한다. 
sns.set_palette('hls',12)                              # hls 팔레트에서 색 12개를 가져온다. 

sns.lineplot(data=df,
             x='year',
             y='passengers',
             hue='month')                              # 값을 그룹핑하는 기준이 되는 컬럼 지정 

plt.show()