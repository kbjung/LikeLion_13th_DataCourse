from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "https://finance.naver.com/sise/sise_index.nhn?code=KOSPI"
page = urlopen(url)
soup = BeautifulSoup(page, "lxml")
# print(soup.title)

# 3-6 실습 - 코스피 정보 가져오기
KOSPI = soup.find(id="now_value")
print("KOSPI :",KOSPI.text)

# 3-6 실습 - 거래량, 장중최고, 52주최고
Que = soup.find(id="quant")
print("거래량(천주) :", Que.text)

High = soup.find(id="high_value")
print("장중 최고가 :", High.text)

table_kos_index = soup.find(class_="table_kos_index").children
# print(table_kos_index)
list1 = list(table_kos_index)
# for i, b in enumerate(list1):
# 	print(i, b)
# 52주 인덱스 : 7
print("52주 최고가 :",list1[7].find(class_="td").text)

# 3-7 (추가) 투자자별 매매동향, 프로그램 매매동향
lst_kor_info = soup.dl
# print(lst_kor_info)
all_info = lst_kor_info.find_all("dd")
# print(all_info[0])


# 개인, 외국인, 기관 매매 동향
print("개인 :", all_info[0].span.text)
print("외국인 :", all_info[1].span.text)
print("기관 :", all_info[2].span.text)

# 프로그램 매매 동향



# 3-8 실습 - 시황뉴스
news = soup.find(class_="sise_report")
lst_news = news.find_all("span", class_="tit")
# print(lst_news)
# print(lst_news[0].text)
n = []
for i in lst_news:
	n.append(i.text)
print(n)

# 3-8 (추가) 시황정보 리포트 정보 가져오기

