# 그룹정보가 있는 두 개 변수의 산점도 

import pandas as pd
import matplotlib.pyplot as plt

# 데이터 읽기
df = pd.read_csv('/Users/wooju-kang/Downloads/data/iris.csv')

# 그룹이 있는 다중 산점도의 작성
dict = {'setosa':'red','versicolor':'green','virginica':'blue'}      # 각 Species 컬럼에 색 부여 
colors = list(dict[key] for key in df.Species)                       # for문을 통해 색을 리스트에 저장  
colors 

df.plot.scatter(x='Petal_Length',                                    # x축 : Petal_Length 
                y='Petal_Width',                                     # y축 : Petal_Width 
                s=30,                                                # 점의 크기 
                c=colors,                                            # 점의 색깔    
                marker='o')                                          # 점의 모양 
plt.show()



# 산점도에 그룹 범례표시 
fig,ax = plt.subplots()

for label , data in df.groupby('Species'):                           # Species 컬럼에서 그룹화한 후 for문으로 설정정보 지정 
    ax.scatter(x=data['Petal_Length'],
               y=data['Petal_Width'],
               s=30,
               c=dict[label],
               marker='o',
               label=label)
    
    print(data)
    

ax.set_xlabel('Petal_Length')
ax.set_ylabel('Petal_Width')
ax.legend('')
fig.show()
