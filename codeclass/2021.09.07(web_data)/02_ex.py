from urllib.request import urlopen
from bs4 import BeautifulSoup

# url
# tag, id, classes
# 다우산업지수, 나스닥 종합, S&P 500

url = "https://finance.naver.com/world/"
page = urlopen(url)

soup = BeautifulSoup(page, "html.parser")
Daw = soup.find("dd", class_="point_status")
fav = Daw.find("strong")
print("다우 산업지수 :", fav.text)