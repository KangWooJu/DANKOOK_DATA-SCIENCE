import seaborn as sns 
import matplotlib.pyplot as plt

flights = sns.load_dataset('flights')
flights.head()

# 피벗 테이블 생성
df = flights.pivot_table(index='month', 
                         columns='year',
                         values='passengers',                    # 데이터로 사용할 컬럼  
                         aggfunc='mean')                         # 데이터 집계함수  
df.head()

# 히트맵 작성
sns.set_theme(rc={'figure.figsize':(8,7)})
sns.heatmap(df)
plt.title('Heatmap of Flight',fontsize = 20)
plt.show() 