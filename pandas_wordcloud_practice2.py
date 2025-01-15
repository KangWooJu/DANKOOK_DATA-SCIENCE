# 구매 패턴 분석

import pandas as pd 
import matplotlib.pyplot as plt
from mlxtend.frequent_patterns import association_rules,apriori 
from mlxtend.preprocessing import TransactionEncoder

# (1) 데이터 준비 
df = pd.read_csv('/Users/wooju-kang/Downloads/data/chipotle.csv')

df.info()
df.head()



# (2) 데이터 탐색 
len(df['Item'].unique())
temp = df[df.item_price == df.item_price.max()]                                  # 음식의 종류  
temp = temp[['Item','item_price']].drop_duplicates()                             # 가장 비싼 음식  
temp 

temp = df[df.item_price ==df.item_price.min()]                                   # 가장 저렴한 음식 
temp = temp[['Item','item_price']].drop_duplicates()
temp 

len(df['Transaction'].unique())                                                  # 트랜잭션 수 

## 많이 판매된 음식 
sales_quantity = df.groupby('Item').count()
sales_quantity = sales_quantity.sort_values('Transaction',ascending=False)
sales_quantity['Transaction']

## 매출상위 10개 상품 
top_ten = sales_quantity.sort_values('Transaction').tail(10)
top_ten = top_ten['Transaction']
top_ten.plot.barh(xlabel='Transaction',                                         
                  ylabel='',
                  title='Top 10 Items',
                  figsize=(9,5))
plt.subplots_adjust(left=0.2)       
plt.show()



# (3) 연관 분석 

## 전처리 
temp = df[['Transaction','Item']].drop_duplicates()
temp = temp.groupby('Transaction')['Item'].apply(list)
temp 

te = TransactionEncoder()                                                        # 트랜잭션 메트릭스를 생성 : 하나의 행은 하나의 트랜잭션을 의미 , 하나의 칼럼은 하나의 상품을 의미
trans_matrix = te.fit(temp).transform(temp) 
trans_matrix

basket = pd.DataFrame(trans_matrix,columns=te.columns_)
basket.head() 

## 연관 규칙 탐색 
freq_item = apriori(df=basket,min_support=0.01,user_colnames=True)               # 지지도가 0.01 이상인 상품 조합을 추출 
freq_item

rules = association_rules(df=freq_item,metric = 'left',min_threshold=1,          # mteric : 연관규칙 선택시 적용할 평가 척도 
                          num_itemsets=len(basket))                              # min_threshold : 연관 규칙 선택을 위한 기준값으로 평가 척도에 따라 값의 범위가 다름 
                                                                                 # num_itemsets : 연관 규칙 생성시 basket에서 몇 개의 트랜잭션을 참조할지 정하기 
 
rules.sort_values('confidence',ascending=False,inplace=True)                 
rules.head(10)
rules.iloc[0,:].transpose()                                                      # 행 열 전환 

