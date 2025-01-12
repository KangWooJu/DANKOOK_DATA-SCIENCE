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



loc = gk.convert_address_to_coordinates('서울 종로구 사직로 161')
loc
map = folium.Map(location=loc,zoom_start=16)                               # location : 마커의 위치 -> 매개변수 [ 위도 , 경도 ]
folium.Marker(location=loc,
              popup='경복궁').add_to(map)                                    # popup : 마커를 클릭 했을 때 표시할 텍스트 -> 매개변수 [ 표시할 문자열 ] 
 
showMap(map)