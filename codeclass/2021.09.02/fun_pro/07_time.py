import time

print("안녕하세요!")
time.sleep(3) # 3초가 멈춤
print("안녕하세요!")
time.sleep(3)
print("안녕하세요!")
time.sleep(3)
print("안녕하세요!")
time.sleep(3)
print("안녕하세요!")
time.sleep(3)

import webbrowser
webbrowser.open("http://google.com")

# 실습
# 내가 자주가는 웹 사이트를 5개 정도 리스트화시키고, 이를 1초 간격으로 웹브라우저로 띄워준다.

my_web = ["http://google.com", "https://www.daum.net/", "https://www.naver.com/", "https://www.youtube.com/", "https://www.hrd.go.kr/"]
for i in my_web:
    time.sleep(1)
    webbrowser.open(i)