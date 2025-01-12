# 다수의 위치에 표시하기 

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


names = ['용두암','성산일출봉','정방폭포',
'중문관광단지','한라산1100고지','차귀도']

addr = ['제주시 용두암길 15',
'서귀포시 성산읍 성산리',
'서귀포시 동홍동 299-3',
'서귀포시 중문동 2624-1',
'서귀포시 색달동 산1-2',
'제주시 한경면 고산리 산 117']

dict = {"names": names, "addr":addr}
df = pd.DataFrame(dict)
df

# 관광지의 좌표를 df에 추가
gk.add_coordinates_to_dataframe(df, 'addr')
df.dtypes

# 문자열 좌표값을 숫자로 변환
df.decimalLatitude = pd.to_numeric(df.decimalLatitude)
df.decimalLongitude = pd.to_numeric(df.decimalLongitude)
df.dtypes

# 지도의 중심점 계산
center = [df.decimalLatitude.mean(),df.decimalLongitude.mean()]
center


# 지도 객체 생성
map = folium.Map(location= center, zoom_start=10)
# 지도에 마커 추가
for i in range(len(df)):
    folium.Marker(location=[df.iloc[i,2], df.iloc[i,3]],
                  icon=folium.Icon(color='red',icon='star')).add_to(map)
showMap(map)

html_start = html='<div \
style="\
font-size: 12px;\
color: blue;\
background-color:rgba(255, 255, 255, 0.2);\
width:85px;\
text-align:left;\
margin:0px;\
"><b>'
html_end = '</b></div>'

for i in range(len(df)):
    folium.Marker(location=[df.iloc[i,2], df.iloc[i,3]],
                  icon=folium.DivIcon(
                      icon_anchor=(0, 0), 
                      html=html_start+df.names[i]+html_end
)).add_to(map)

showMap(map)