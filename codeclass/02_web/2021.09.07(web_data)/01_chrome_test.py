from urllib.request import urlopen
from bs4 import BeautifulSoup

## 01 우리가 가져올 URL
## 02 원하는 정보의 위치(span id)
## url : https://finance.naver.com/sise/
## tag : span, id : KOSPI_now

## html 코드를 요청해서 가져온다.
url = "https://finance.naver.com/sise/"
page = urlopen(url)
print(page)

## 구체적인 html 확인하고, 구조화
soup = BeautifulSoup(page, "html.parser")
KOSPI = soup.find("span", id="KOSPI_now")
print("코스피 현재 지수 :", KOSPI.text)

# 6-3 (추가) 코스닥 지수, KOSPI200 지수 가져오기
## 코스닥, KOSPI200지수 가져오기
KOSDAQ = soup.find("span", id="KOSDAQ_now")
print("코스닥 현재 지수 :", KOSDAQ.text)

## KOSPI200지수 가져오기
KPI200 = soup.find("span", id="KPI200_now")
print("KOSPI200 현재 지수 :", KPI200.text)

# 6-3 (추가) 인기 검색 종목과 가격 가져오기
fav = soup.find("ul", id="popularItemList")
name = fav.find_all("a")
num = fav.find_all("span")
# print(num)

rank = 0
for i in range(10):
	rank += 1
	print(rank, "위 :", name[i].text, num[i*2].text, "원", num[i*2-1].text)

# 6-3 (추가) 인기 검색 종목과 가격 가져오기(해설)
# data = soup.find("ul", class_="lst_pop")
# dat_all = data.find_all("a")
# value_all = data.find_all("span")
#
# for one in dat_all:
# 	print(one.text)
#
# for one in value_all:
# 	print(one.text)