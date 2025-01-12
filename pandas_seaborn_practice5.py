import matplotlib.pyplot as plt
import seaborn as sns 
from statsmodels.graphics.mosaicplot import mosaic

plt.rcParams['font.family'] = 'AppleGothic'
plt.rcParams['axes.unicode_minus'] = False

# 데이터 준비 
df = sns.load_dataset('titanic')
df.head()
dict1 = {0:'사망',1:'생존'}
dict2 = {'male':'남성','female':'여성'}

df = df.replace({'survived':dict1})
df = df.replace({'sex':dict2})
df.head()

# 그래프 설정 
props = lambda key : {'color':'lightgreen' if '생존' in key else 'yellow'}

# 그래프 작성
mosaic(data=df.sort_values('sex'),
       index=['sex','survived'],
       properties = props,                                                     # 타일 색상 변경   
       axes_label = True,                                                      # 축 레이블 표시  
       title='타이타닉 남녀 생존비율')                                              # 그래프 제목  

plt.show()
