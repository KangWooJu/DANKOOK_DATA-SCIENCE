import seaborn as sns 
import matplotlib.pyplot as plt 

df = sns.load_dataset('flights')
df.head()

# 그래프 테마 설정 
sns.set_theme(style="whitegrid",
              rc={"figure.figsize":(8,5)})
sns.set_palette('hls',12)

sns.lineplot(data=df,
             x='year',
             y='passengers',
             hue='month')

plt.show()