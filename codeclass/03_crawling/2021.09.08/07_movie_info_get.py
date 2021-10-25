from bs4 import BeautifulSoup
from urllib.request import urlopen

# url 정보
# tag, id, class 정보

# url 가져와서 b4로 담기
url = "https://movie.naver.com/movie/running/current.naver#"
page = urlopen(url)
soup = BeautifulSoup(page, "lxml")
# print(soup.title) # 가져오기 정보 확인

# 6-4 실습 - 타이틀 정보 가져와 보기
# my sol.
title_info = soup.find_all("dt", class_="tit")
# print(title_info)
title_lst = []
for i in title_info:
	j = i.find("a").text
	title_lst.append(j)
print(title_lst, len(title_lst),"개")

# sol.
# title_all_data = soup.find("dt", class_="tit")
#
# list_all = []
# for one in title_all_data:
# 	title_one = one.find("a").text
# 	list_all.append(title_one)
# print(list_all)

# 6-5 실습 - 평점 점수 가져오기
# my sol.(마지막 두 번째 자료 다름.)
rate_all = soup.find_all("dl", class_="info_star")
# print(rate_all)
# print(rate_all[0].find(class_="num"))
# print(len(rate_all))
rate_lst = []
for i in rate_all:
	j = i.find("span", class_="num").text
	rate_lst.append(j)
print(rate_lst)

# # sol.
# score_all = soup.find_all("dl", class_="info_star")
# # print(score_all[2].find("span", class_="num").text)
#
# all_score = []
# for one in score_all:
# 	one_score = one.find("span", class_="num").text
# 	# print(one_score)
# 	all_score.append(one_score)
# print(all_score)

# 7-2 예매율 정보 가져오기
# my sol.
a_all = soup.find_all("div", class_="star_t1 b_star")
# print(a_all)
a_lst = []
for i in a_all:
	a_lst.append(i.find("span", class_="num").text)

print(a_lst)

# # sol.
# rate_tmp = soup.find_all("dl", class_="info_exp")
# rate_all_all = []
# for one in rate_tmp:
# 	one_rate = one.find("span", class_="num").text
# 	rate_all_all.append(one_rate)
# print(rate_all_all)

# 7-3 참여 명수 가져오기(...)
# my sol.
p_all = soup.find_all("dl", class_="info_star")
print(p_all[0].find("em").text)
p_lst = []
for i in p_all:
	j = i.find("em").text
	p_lst.append(j)

print(p_lst)

# # sol.
# num_people = soup.find_all("dl", class_="info_star")
#
# num_all = []
# for one in num_people:
# 	one_data = one.find("em").text
# 	num_all.append(one_data)
#
# print("참여 명수", num_all)

# 타이틀, 평점, 평점 참여 명수, 예메율
# 파일 만들기
import pandas as pd
# title_lst, rate_lst, p_lst
dict_data = {"영화제목":title_lst, "평점":rate_lst, "평점 참여 명수":p_lst}

data = pd.DataFrame(dict_data)
data.to_csv("naver_movie_info.csv", index=False)
data.to_exel("naver_movie_info.xlsx", index=False)