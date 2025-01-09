import pandas as pd
import seaborn as sns 
import matplotlib.pyplot as plt 

df = pd.read_csv('/Users/wooju-kang/Downloads/data/crimeRatesByState2005.csv')
df.head()

# 버블 차트 
sns.set_theme(rc={'figure.figsize':(7,7)})
sns.scatterplot(
    data=df,
    x='murder',                                                               # x 축 
    y='burglary',                                                             # y 축 
    size='population',                                                        # 원의 크기 
    sizes=(20,4000),                                                          # 원의 크기 범위  
    hue='state',                                                              # 원의 색   
    alpha=0.5,                                                                # 투명도  
    legend=False                                                              # 범례표시 여부   
)
plt.xlim(0,12)                                                                # x축 값의 범위  

# 주 이름을 버블 위에 표시 
for i in range(0,df.shape[0]):
    plt.text(x=df.murder[i],y=df.burglary[i],s=df.state[i],
             horizontalalignment='center',
             size='small',
             color='dimgray')

plt.show()