import pandas as pd
import matplotlib.pyplot as plt

colors = pd.Series([2,3,2,1,1,2,2,1,3,2,1,3,2,1,2,])

fd = colors.value_counts()
fd.index
fd.index = ['red','green','blue']
fd

# 막대 그래프 출력
fd.plot.bar(xlabel='Color',
            ylabel='Frequency',
            rot=0,
            title='Favorite Color')

plt.show()


# 원 그래프 출력
fd.plot.pie(ylabel='',
            autopct='%1.0f%%',
            title='Favorite Color')
plt.show()

