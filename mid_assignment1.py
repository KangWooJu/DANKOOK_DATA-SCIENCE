import pandas as pd
import matplotlib.pyplot as plt  
import displayMap
import folium
import geokakao as gk
import os
import webbrowser
import seaborn as sns 

plt.rcParams['font.family'] = 'AppleGothic'            # 한글 폰트 변경  
plt.rcParams['axes.unicode_minus'] = False               # 마이너스부호 깨짐 방지 

def showMap(map):
    """
    folium 지도 객체를 HTML 파일로 저장한 후, 웹 브라우저로 열어주는 함수.
    """
    map.save("map.html")  # 지도 객체를 'map.html'로 저장
    filepath = os.getcwd()  # 현재 작업 디렉토리 경로 가져오기
    file_uri = 'file:///' + filepath + '/map.html'  # 파일 URI 생성
    webbrowser.open_new_tab(file_uri)  # 새 탭에서 파일 열기



# 문제 1
## 5개의 파일 병합하기 
data1 = pd.read_csv('/Users/wooju-kang/Downloads/data/seoul_201512.csv')
data2 = pd.read_csv('/Users/wooju-kang/Downloads/data/seoul_201606.csv')
data3 = pd.read_csv('/Users/wooju-kang/Downloads/data/seoul_201612.csv')
data4 = pd.read_csv('/Users/wooju-kang/Downloads/data/seoul_201706.csv')
data5 = pd.read_csv('/Users/wooju-kang/Downloads/data/seoul_201712.csv')



df12 = pd.concat([data1,data2])
df34 = pd.concat([data3,data4])
df345 = pd.concat([df34,data5])
df12345 = pd.concat([df12,df345])
df12345

## 행의 개수와 열의 개수 
df12345.shape[0]
df12345.shape[1]

## 앞쪽 5개의 행 보이게 하기 
df12345.head(5)




# 2번 
## 2017년 12월 수집 데이터에 대해 상권업종대분류명 기준으로 업소 수 합계를 보이게 하기 
data_2 = data5['상권업종대분류명']
data_2
len(data_2)





# 3번
## 2017년 12월 수집 데이터에 대해 상권업종대분류명 기준으로 업소 수를 막대그래프로 나타내기 
# 막대 그래프 출력

data_3 = data5['상권업종대분류명']

data_3_veri = data_3.value_counts()

data_3_veri.plot.bar(xlabel='상권업종대분류명',rot=0,figsize=(10,10),title='')
plt.subplots_adjust(bottom=1)
plt.show()



# 4번
## 2017년 12월 수집 데이터에 대해 점포수가 많은 상위 10개 동 

data_4 = data5['행정동명'].value_counts()
data_4.head(10)



# 5번
## 수집년월에 따른 점포수의 변화를 선 그래프로 나타내시오 
len(data1)
number5 = pd.Series([len(data1),len(data2),len(data3),len(data4),len(data5)],index=list(range(1,6)))
number5.plot(xlabel='연도추이',ylabel='점포수',linestyle='solid',marker='o')
plt.show()





# 측정위치에 마커 표시하기
for i in range(len(data_6)):
    folium.Marker(location=[data_6['위도'].iloc[i], data_6['경도'].iloc[i]],
                  icon=folium.Icon(color='blue', icon='flag')).add_to(map)
showMap(map)

#7번
## 2017년 12월 수집 데이터에 대해 구별 점포 수를 지도에 원의 크기로 나타내시오 

### displayMap 사용하기 

data_sigungu = data5['시군구명'].value_counts()

df = data5.sample(len(data5),random_state=123)
color_get = sns.set_palette('hls',50)

# 지도의 중심점 구하기
center = [df['위도'].mean(), df['경도'].mean()]
map = folium.Map(location=center, zoom_start=5) # 마커 없는 지도

# 측정위치에 마커 표시하기
for i in range(len(df)):
    folium.Marker(location=[df['위도'].iloc[i], df['경도'].iloc[i]],
                  icon=folium.Icon(color='blue', icon='flag')).add_to(map)

# 원의 크기로 표시하기
for i in range(len(df)):
    folium.CircleMarker(location=[df['위도'].iloc[i], df['경도'].iloc[i]],
                        radius=2, # 원의 반지름
                        color='red', # 원의 색
                        stroke=False, #명윤곽선 없음
                        fill=True, # 원의 내부 색
                        fill_opacity='50%' # 원의 도부색 투명도
                        ).add_to(map)
    
showMap(map)