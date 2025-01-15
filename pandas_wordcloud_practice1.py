import pandas as pd 
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import konlpy

# (1) 데이터 준비 
df = pd.read_csv('/Users/wooju-kang/Downloads/data/movie1_review.csv')
df




# (2) 형태소 분석기 정의 
kkma =konlpy.tag.Kkma()                              # 형태소 분석기 꼬꼬마(Kkma) -> 조사가 붙어있을 경우 이 둘을 분리하여 따로 정리한다. 





# (3) 단어 데이터프레임 만들기 
nouns = df['Review'].apply(kkma.nouns)                                         # 명사 (nouns ) 추출   
nouns 
nouns = nouns.explode()                                                        # 리스트 형태의 값을 여러 행으로 전개하는 메소드  




# (4) 전처리 실시 



## 모시 -> 티모시 , imax -> 아이맥스 등 : 불완전한 & 불필요한 단어들을 정리 
nouns[nouns=='모시'] = '티모시'
nouns[nouns=='IMAX'] = '아이맥스'
nouns[nouns=='파트3'] = '3편'

## 글자수 2개 이상인 단어만 추출 
df_word = pd.DataFrame({'word':nouns})
df_word['count'] = df_word['word'].str.len()
df_word = df_word.query('count>=2')
df_word 

## 단어 빈도수 집계 및 정렬 
df_word = df_word.groupby('word',as_index = False)                             # 단어를 기준으로 그룹핑 
df_word = df_word.count().sort_values('count',ascending = False)               # 그룹 연산의 결과를 인덱스가 아닌 정규 컬럼으로 반환  
df_word 

## 불필요한 단어 제거

del_idx = df_word.loc[df_word.word.isin(['영화','편이','영화관'                    # 의미 없다고 판단되는 단어들은 제거 
                                         ,'파트'])].index 
 
df_word = df_word.drop(index=del_idx)




# (5) 워드클라우드 만들기 

## 빈도수 상위 10개 단어 
plt.rcParams['font.family'] = 'AppleGothic'
plt.rcparams['axes.unicode_minus'] = False 

df_top10 = df_word.iloc[:10,:].sort_values('count',ascending=True)
df_top10.plot.barh(x='word',y='count')
plt.show() 

## 워드 클라우드
dic_word = df_word.set_index('word').to_dict()['count']
dic_word 

wc = WordCloud(random_state=123,
               font_path='',
               width=400,
               height=400,
               background_color='white')

img_worldcloud = wc.generate_from_frequencies(dic_word)                       # 워드클라우드를 이미지로 변환하기 

plt.figure(figsize=(10,10))                                                   # 크기 지정하기  
plt.axis('off')                                                               # 축 없애기  
plt.imshow(img_worldcloud)                                                    # 결과 보여주기  
plt.show()                                                                    # 결과를 화면에 출력 



# (6) 워드클라우드를 원하는 모양으로 바꾸기 

import PIL
import numpy as np

icon = PIL.Image.open('').convert("RGBA")
img = PIL.Image.new(mode = "RGBA",size=icon.size,color=(255,255,255))
img.paste(icon,icon)
img = np.array(img)

wc = WordCloud(random_state=123,
               font_path='폰트위치',
               width=400,
               height=400,
               background_color='white',
               mask=img,
               colormap='inferno')

img_worldcloud = wc.generate_from_frequencies(dic_word)                        # 워드클라우드 -> 이미지  


plt.figure(figsize = (10,10))                                                  # 크기 지정하기  
plt.axis('off')                                                                # 축 없애기  
plt.imshow(img_worldcloud)                                                     # 결과 보여주기  
plt.show()                                                                     # 결과를 화면에 출력하기 
 
