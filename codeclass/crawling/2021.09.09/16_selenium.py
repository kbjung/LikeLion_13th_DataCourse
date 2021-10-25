from urllib.request import urlopen
from bs4 import BeautifulSoup

# # 옥션 데이터 정보 가져오기
# url = "http://www.auction.co.kr/"
# page = urlopen(url)
# soup = BeautifulSoup(page, "lxml")
# print(soup.title)

# # 옥션 데이터 정보 가져오기
# url = "http://browse.auction.co.kr/search?keyword=%EA%B0%80%EB%B0%A9&itemno=&nickname=&frm=hometab&dom=auction&isSuggestion=No&retry=&Fwk=%EA%B0%80%EB%B0%A9&acode=SRP_SU_0100&arraycategory=&encKeyword=%EA%B0%80%EB%B0%A9"
# page = urlopen(url)
# soup = BeautifulSoup(page, "lxml")
# print(soup.title)
# print(soup.find_all("span", class_="text--title"))
#
# # 롯데 ON
# url = "https://www.lotteon.com/search/search/search.ecn?render=search&platform=pc&q=%EA%B0%80%EB%B0%A9&mallId=1"
# page = urlopen(url)
# soup = BeautifulSoup(page, "lxml")
# print(soup.title)
# print(soup.find_all("div", class_="srchProductUnitTitle"))
#
# # 스타일난다
# url = "https://stylenanda.com/product/search.html?sort_method=6&x=0&y=0&keyword=%EA%B0%80%EB%B0%A9"
# page = urlopen(url)
# soup = BeautifulSoup(page, "lxml")
# print(soup.title)

from selenium import webdriver
driver = webdriver.Chrome("./data/chromedriver")