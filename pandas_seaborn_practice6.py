import seaborn as sns 
import matplotlib.pyplot as plt

flights = sns.load_dataset('flights')
flights.head()

# 피벗 테이블 생성
df = flights.pivot_table(index='month',
                         columns='year',
                         values='passengers',
                         aggfunc='mean')
df.head()

# 히트맵 작성
sns.set_theme(rc={'figure.figsize':(8,7)})
sns.heatmap(df)
plt.title('Heatmap of Flight',fontsize = 20)
plt.show() 