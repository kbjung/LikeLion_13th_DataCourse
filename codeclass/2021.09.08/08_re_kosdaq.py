from urllib.request import urlopen
from bs4 import BeautifulSoup

# url을 bs로 담기
url = "https://finance.naver.com/sise/sise_index.nhn?code=KOSDAQ"
page = urlopen(url)
soup = BeautifulSoup(page, "lxml")

all_info = []
# KOSDAQ 지수
kosdaq = soup.find("em",id="now_value").text
print("KOSDAQ :", kosdaq)
all_info.append(kosdaq)

# 거래량(천주), 장중최고, 52주 최고
flu = soup.find(id="quant").text
print("거래량(천주) :", flu)
all_info.append(flu)

high = soup.find(id="high_value").text
print("장중최고 :", high)
all_info.append(high)

all_y_high = soup.find("table", class_="table_kos_index")
# all_y_high2 = all_y_high.find_all("tr")[2]
# highest = all_y_high2.find("td", class_="td").text
all_y_high2 = all_y_high.find_all("tr")[2].find("td", class_="td").text
print("52주 최고 :", all_y_high2)
all_info.append(all_y_high2)
print(all_info)

## 파일로 만들기
## 리스트 형태
## {key1:[a,b,c,d]}

import pandas as pd

info_list = ['코스닥지수', '거래량(천주)', '장중최고', '52주최고']

dic_dict = {"구분" : info_list, "코스닥 정보" : all_info} # 리스트의 길이는 같아야 한다.
dat = pd.DataFrame(dic_dict)
dat.to_csv("08_re_kosdaq.csv", index=False)
dat.to_excel("08_re_kosdaq.xlsx", index=False)
# 한 리스트는 열로 배열된다.