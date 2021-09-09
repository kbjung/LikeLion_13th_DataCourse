from bs4 import BeautifulSoup
from urllib.request import urlopen
import pandas as pd

# 함수(my sol)
# 해당 페이지 댓글 가져오기 함수
def cmt(a):
	url = f"https://movie.naver.com/movie/point/af/list.naver?st=mcode&sword=171725&target=after&page={a}"
	page = urlopen(url)
	soup = BeautifulSoup(page, "html.parser")

	comment_all = soup.find_all("td", class_="title")
	return comment_all

	lst = []
	for one in comment_all:
		temp = list(one.children)[6].strip()
		comments.append(temp)


lst = []
for i in range(1, 6):
	lst.append(cmt(i))

dat_dict = {"댓글" : lst}
dat = pd.DataFrame(dat_dict)
dat.to_csv("my_reply.csv", index=False)
dat.to_excel("my_reply.xlsx", index=False)