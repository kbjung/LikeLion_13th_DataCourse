from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd

url = "https://finance.naver.com/sise/sise_index.nhn?code=KOSPI"
page = urlopen(url)
soup = BeautifulSoup(page, "lxml")

# 4-2 시황 뉴스 - excel파일, csv파일 만들기
# 코스피 정보, 거래량(천주), 장중최고, 52주 최고, 시황뉴스

news = soup.find(class_="sise_report")
lst_news = news.find_all("span", class_="tit")

news = []
for i in lst_news:
	news.append(i.text)
# print(n)
dat = pd.DataFrame({"시황뉴스": news})
print(dat)
dat.to_csv("news.csv", index=True)
dat.to_excel("news_excel.xlsx", index=False)