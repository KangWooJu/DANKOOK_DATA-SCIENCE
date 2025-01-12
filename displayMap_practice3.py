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



loc = gk.convert_address_to_coordinates('전주시 완산구 홍산로 390')
print(loc)
map = folium.Map(location=loc,zoom_start=13)                               # location : 마커의 위치 -> 매개변수 [ 위도 , 경도 ]
folium.Marker(location=loc,
             icon=folium.Icon(color='red',icon='star')).add_to(map)        # 마커 표시 
 


showMap(map)

html_start = html = '<div \
style="\
font-size: 12px;\
color: blue;\
background-color:rgba(255, 255, 255, 0.2);\
width:85px;\
text-align:left;\
margin:0px;\
"><b>'

html_end = '</b></div>'

folium.Marker(location=loc,
              icon=folium.DivIcon(
                  icon_anchor=(0,0),
                  html=html_start+'우리집'+html_end
              )).add_to(map)


showMap(map)