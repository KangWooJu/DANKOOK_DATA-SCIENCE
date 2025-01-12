import pandas as pd 
import folium
import geokakao as gk
import webbrowser
import os
os.chdir('/Users/wooju-kang/Desktop/DANKOOK_DATA SCIENCE')
import displayMap as dm 


def showMap(map):
    """
    folium 지도 객체를 HTML 파일로 저장한 후, 웹 브라우저로 열어주는 함수.
    """
    map.save("map.html")  # 지도 객체를 'map.html'로 저장
    filepath = os.getcwd()  # 현재 작업 디렉토리 경로 가져오기
    file_uri = 'file:///' + filepath + '/map.html'  # 파일 URI 생성
    webbrowser.open_new_tab(file_uri)  # 새 탭에서 파일 열기

df = pd.read_csv('/Users/wooju-kang/Downloads/data/wind.csv')
df.head()

df =df.sample(50,random_state=123)

# 지도의 중심점 구하기
center = [df.lat.mean(), df.lon.mean()]


# 지도 가져오기
map = folium.Map(location=center, zoom_start=5)
showMap(map)

# 측정위치에 마커 표시하기
for i in range(len(df)):
    folium.Marker(location=[df.lat.iloc[i], df.lon.iloc[i]],
                  icon=folium.Icon(color='blue', icon='flag')).add_to(map)
showMap(map)

# 풍속을 원의 크기로 표시하기
map = folium.Map(location=center, zoom_start=5) # 마커 없는 지도
for i in range(len(df)):
    folium.CircleMarker(location=[df.lat.iloc[i], df.lon.iloc[i]],
                        radius=(df.spd.iloc[i]**0.5)*2, # 원의 반지름
                        color='red', # 원의 색
                        stroke=False, # 윤곽선 없음
                        fill=True, # 원의 내부 색
                        fill_opacity='50%' # 원의 내부색 투명도
                        ).add_to(map)
    
showMap(map)