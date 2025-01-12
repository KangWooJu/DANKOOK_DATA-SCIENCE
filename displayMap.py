import webbrowser
import os

def showMap(map):
    """
    folium 지도 객체를 HTML 파일로 저장한 후, 웹 브라우저로 열어주는 함수.
    """
    map.save("map.html")  # 지도 객체를 'map.html'로 저장
    filepath = os.getcwd()  # 현재 작업 디렉토리 경로 가져오기
    file_uri = 'file:///' + filepath + '/map.html'  # 파일 URI 생성
    webbrowser.open_new_tab(file_uri)  # 새 탭에서 파일 열기
