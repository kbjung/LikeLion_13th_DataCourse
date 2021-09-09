# 코스닥 정보에 대한
# 6-1,2 지수 정보 20210908_index.csv
# 6-3 시황정보 뉴스 20210908_news.csv
# 6-3 시황정보 리포트 20210908_report.csv
# 6-4 인기검색어 20210908_pop_word.csv
# 6-5 가장 많이 본 뉴스 20210908_cnt_news.csv

# (추가) 함수로 정리
# 6-6 (도전) 여러 파일을 하나로 병합시키기
# 6-7 (도전) github정리 및 함수 - github올리고 링크 댓글 올리기

# 라이브러리 가져오기
from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd

# 주소에서 파일 가져오기
url = "https://finance.naver.com/sise/sise_index.nhn?code=KOSDAQ"
page = urlopen(url)
soup = BeautifulSoup(page, "html.parser")

# 6-1. 지수 정보 20210908_index.csv
# id : now_value
KOSDAQ = soup.find(id="now_value")
print("KOSDAQ :", KOSDAQ.text)
KOSDAQ_l = []
KOSDAQ_l.append(KOSDAQ.text)

	# 6-2 지수 파일 만들기
dat = pd.DataFrame({"시황뉴스": KOSDAQ_l})
dat.to_csv("20210908_index.csv", index=False)

# 6-3. 시황정보 뉴스 20210908_news.csv
news = soup.find(class_="sise_report")
c_news = news.find_all(class_="tit")
news_l = []
for i in c_news:
	news_l.append(i.text)
	# 시황 파일 만들기
news_d = pd.DataFrame({"시황뉴스":news_l})
news_d.to_csv("20210908_news.csv", index=True)

# 6-3. 시황정보 리포트 20210908_report.csv

news_all = soup.find_all(class_="sise_report")
# print(len(news_all))
news_report = news_all[1]
c_news_report = news_report.find_all(class_="tit")
# print(c_news_report)
news_report_l = []
for i in c_news_report:
	news_report_l.append(i.text)
# print(news_report_l)

news_report_d = pd.DataFrame({"시황 뉴스 리포트":news_report_l})
news_report_d.to_csv("20210908_report.csv", index=True)

# 6-4. 인기검색어 20210908_pop_word.csv

fav_all = soup.find_all("a", class_="company")
fav_l = []
for i in fav_all:
	fav_l.append(i.text)
# print(fav_l)
fav_d = pd.DataFrame({"인기검색어":fav_l})
fav_d.to_csv("20210908_fav.csv", index=True)

# 6-5. 가장 많이 본 뉴스 20210908_cnt_news.csv
fre = soup.find(class_="right_list_1_2")
# print(fre_all)
fre_all = fre.find_all("a")
# print(fre_all)
fre_l = []
for i in fre_all:
	fre_l.append(i.text)
# print(fre_l)
fre_d = pd.DataFrame({"가장 많이 본 뉴스":fre_l})
fre_d.to_csv("20210908_fre.csv", index=True)