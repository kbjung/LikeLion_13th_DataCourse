# from bs4 import BeautifulSoup
# from urllib.request import urlopen
# import pandas as pd
#
# # my sol.
# basic_url = "https://movie.naver.com/movie/point/af/list.naver?st=mcode&sword=171725&target=after&page="
# for i in range(1,6,1):
# 	real_url = basic_url + str(i)
# 	page = urlopen(real_url)
# 	soup = BeautifulSoup(page, "html.parser")
# 	comment_all = soup.find_all("td", class_="title")
#
# 	comments = []
# 	for one in comment_all:
# 		temp = list(one.children)[6].strip()
# 		comments.append(temp)
# 	print(comments)

from bs4 import BeautifulSoup
from urllib.request import urlopen
import pandas as pd

# sol.
## 1~5페이지 가져오기
## 댓글 1페이지의 댓글 전체 가져오기-10개
basic_url = 'https://movie.naver.com/movie/point/af/list.naver?st=mcode&sword=171725&target=after&page='

comment_5 = []
for i in range(1,6,1):
	real_url = basic_url + str(i)
	page = urlopen(real_url)
	soup = BeautifulSoup(page, 'html.parser')
	comment_all = soup.find_all('td', class_ = 'title')
	print(len(comment_all))

	# comments = []
	for one in comment_all:
		temp = list(one.children)[6].strip()
		comment_5.append(temp)

dict_dat = {"댓글" : comment_5}
dat = pd.DataFrame(dict_dat)
dat.to_csv("댓글_5.csv", index=False)
dat.to_excel("댓글_5.xlsx", index=False)