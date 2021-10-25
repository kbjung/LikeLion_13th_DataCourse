from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd
import time

basic_url = "https://movie.naver.com/movie/point/af/list.naver?st=mcode&sword=201073&target=after&page="

lst = []
for i in range(1,35):
	real_url = basic_url + str(i)
	page = urlopen(real_url)
	soup = BeautifulSoup(page, "html.parser")
	comment_all = soup.find_all("td", class_="title")

	for one in comment_all:
		two = list(one.children)[-3].strip()
		lst.append(two)
	time.sleep(1)

dict_dat = {"댓글" : lst}
dat = pd.DataFrame(dict_dat)
dat.to_csv("코다댓글.csv", index=False)
dat.to_excel("코다댓글.xlsx", index=False)
