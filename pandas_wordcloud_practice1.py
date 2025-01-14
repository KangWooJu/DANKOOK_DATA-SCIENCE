import pandas as pd 
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import konlpy

# (1) 데이터 준비 
df = pd.read_csv()
df

# (2) 형태소 분석기 정의 
kkma =konlpy.tag.Kkma()                              # 형태소 분석기 꼬꼬마(Kkma)

# (3) 단어 데이터프레임 만들기 
nouns = df['Review'].apply(kkma.nouns)               # 명사 추출  
nouns 

# (4) 전처리 실시 

# 모시 -> 티모시 , imax -> 아이맥스 등 
nouns[nouns=='모시'] = '티모시'
nouns[nouns=='IMAX'] = '아이맥스'
nouns[nouns=='파트3'] = '3편'

# 글자수 2개 이상인 단어만 추출 
df_word = pd.DataFrame({'word':nouns})
df_word['count'] = df_word['word'].str.len()
df_word = df_word.query('count>=2')
df_word 

# 단어 빈도수 집계 및 정렬 
df_word 