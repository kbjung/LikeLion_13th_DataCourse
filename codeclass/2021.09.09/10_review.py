from bs4 import BeautifulSoup
from urllib.request import urlopen
import pandas as pd

# 댓글 1개 가져오기

url = "https://movie.naver.com/movie/point/af/list.naver?st=mcode&sword=171725&target=after"

page = urlopen(url)
soup = BeautifulSoup(page, "html.parser")
print(soup.title)

# 댓글 하나 가져와 보기
c_all = soup.find_all("td", class_="title")
# print(len(c_all))
# print(c_all[0])
dat = list(c_all[2].children)
# dat_comment = dat[6].replace("\n", "")
# dat_comment = dat_comment.replace("\t", "")
dat_comment = dat[6].strip() # .strip() : 계행(\n, \t, \r)을 모두 제거해준다.
print(len(dat))
print(dat_comment)

# 댓글 1페이지의 댓글 전체 가져오기 - 10개
comment_all = soup.find_all("td", class_="title")
print(len(comment_all))

# 2페이지 가져오기

url2 = "https://movie.naver.com/movie/point/af/list.naver?st=mcode&sword=171725&target=after&page=2"
page2 = urlopen(url2)
soup2 = BeautifulSoup(page2, "html.parser")
print(soup2.title)

comment_all2 = soup2.find_all("td", class_="title")
comments2 = []
for one in comment_all2:
	temp = list(one.children)[6].strip()
	# print(temp)
	comments2.append(temp)
# print(comments2)

comments = []
for one in comment_all:
	temp = list(one.children)[6].strip()
	# print(temp)
	comments.append(temp)
# print(comments)

dict_dat = {"영화댓글" : comments, "2페이지 댓글": comments2}
dat = pd.DataFrame(dict_dat)
dat.to_csv("댓글.csv", index=False)
dat.to_excel("댓글.xlsx", index=False)
