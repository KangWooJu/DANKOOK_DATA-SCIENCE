import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset('tips')
df.head


# 그래프 테마 설정
sns.set_theme(style="whitegrid",rc={"figure.figsize":(5,5)})

# 요일별 평균 지불금액
sns.barplot(data=df,                                               # df 이름  
            x='day',                                               # x축 컬럼  
            y='total_bill',                                        # y축 컬럼  
            estimator='mean',                                      # y축 컬럼 적용 함수  
            hue='day',                                             # y축 값의 그룹핑 기준  
            legend=None)                                           # 에러선 삭제   

plt.show()

