import folium
import geokakao as gk
import os
import webbrowser
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


print(dm)
print(dir(dm))

# 지도 중심의 좌표를 알 때  
loc = [37.54,127.05]                                                           # 위도 , 경도 
map = folium.Map(location=loc)                                                 # 지도 객체 생성 
showMap(map)                                                                # 웹브라우저에 지도 표시 

# 지도 중심의 주소를 알 때 
loc = gk.convert_address_to_coordinates('경기 용인시 수지구 죽전로 152')
loc                                                                            # 지도의 중심좌표  
map = folium.Map(location=loc,zoom_start=16)                                   # 지도 객체 생성  
showMap(map)                                                                # 웹브라우저에 지도 표시  