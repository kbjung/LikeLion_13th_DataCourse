from urllib.request import urlopen
from bs4 import BeautifulSoup

# 웹 페이지 소스 가져오기 및 파싱
url = "https://movie.naver.com/movie/running/current.naver"
page = urlopen(url)
soup = BeautifulSoup(page, "lxml")

# 제대로 불러왔는지 확인
print(soup.title)

# 상영작/예정작 제목만 뽑기
soup_ul_li = soup.find("ul", class_="lst_detail_t1").find_all("li")

# 영화 개수 확인
print(len(soup_ul_li))
# 1번째 영화 제목 출력 확인
print(soup_ul_li[0].find("dt", class_="tit").a.text)
# 5번째 영화 제목 출력 확인
print(soup_ul_li[4].find("dt", class_="tit").a.text)
# 123번째(마지막) 영화 제목 출력 확인
print(soup_ul_li[122].find("dt", class_="tit").a.text)

# 평점
# 출력 확인
print(soup_ul_li[0].find("span", class_="num").text)

# 참여 명수
# 출력 확인
print(soup_ul_li[0].find("em").text)

# 예매율
# print(soup_ul_li[0].find("dl", class_="info_exp").span.text)
temp = soup_ul_li[122].find("dl", class_="info_exp")
if temp is not None:
	t = temp.span.text
	print("값이 있음.", t)
else:
	t = 0
	print("값이 없음.", t)

# # 개요
# print(soup_ul_li[0].find("span", class_="link_txt").text)
# txt = soup_ul_li[0].find("span", class_="link_txt").text
# txt_last = txt.replace("\n", "")
# txt_last = txt_last.replace("\t", "")
# txt_last = txt_last.replace("\r", "")
# print(txt_last)

# # 2-3 (추가) 기타 정보(감독, 출연, 상영시간) 추가 후 - 댓글 달기
# # 감독
# director = soup_ul_li[122].find("dl", class_="info_txt1").find_all("dd")[1].text
# # print(director)

# 출연
# actor = soup_ul_li[10].find("dl", class_="info_txt1").find_all("dd")[-1].text
# print(actor)
# lst = []
# for one in soup_ul_li:
# 	actor = one.find("dl", class_="info_txt1").find_all("dd")[-1].text
# 	txt_a = actor.replace("\n", "")
# 	txt_a = txt_a.replace("\t", "")
# 	txt_a = txt_a.replace("\r", "")
# 	lst.append(txt_a)
# print(len(lst))

# 상영시간(...)
time = soup_ul_li[0].find("dl", class_="info_txt1").find_all("dd")[0].text
print(time)


# # 제목, 평점, 참여수, 개요, 감독, 출연
# all_title = []
# all_score = []
# all_people = []
# all_rate = []
# all_category = []
# all_director = []
# all_actor = []
#
# for one in soup_ul_li:
# 	title = one.find("dt", class_="tit").a.text
# 	score = one.find("span", class_="num").text
# 	num_people = one.find("em").text
#
# 	# 예매율
# 	tmp = one.find("dl", class_="info_exp")
# 	if tmp is not None:
# 		rate = tmp.span.text
# 	else:
# 		rate = 0
#
# 	# 카테고리 빈공간 정리
# 	category = one.find("span", class_="link_txt").text
# 	txt_last = category.replace("\n", "")
# 	txt_last = txt_last.replace("\t", "")
# 	txt_last = txt_last.replace("\r", "")
#
# 	# 감독 빈공간 정리
# 	director = one.find("dl", class_="info_txt1").find_all("dd")[1].text
# 	txt_d = director.replace("\n", "")
# 	txt_d = txt_d.replace("\t", "")
# 	txt_d = txt_d.replace("\r", "")
#
# 	# 출연 빈공간 정리
# 	actor = one.find("dl", class_="info_txt1").find_all("dd")[-1].text
# 	txt_a = actor.replace("\n", "")
# 	txt_a = txt_a.replace("\t", "")
# 	txt_a = txt_a.replace("\r", "")
#
# 	all_title.append(title)
# 	all_score.append(score)
# 	all_people.append(num_people)
# 	all_rate.append(rate)
# 	all_category.append(txt_last)
# 	all_director.append(txt_d)
# 	all_actor.append(txt_a)
#
# print(len(all_title),len(all_score), len(all_people),len(all_rate), len(all_category), len(all_director), len(all_actor))
#
# # 저장을 위한 csv, xlsx 파일 만들기
# import pandas as pd
#
# dat_dict = {
# 	"제목" : all_title, "평점" : all_score, "참여 명수" : all_people, "예매율" : all_rate, "개요" : all_category, "감독" : all_director, "출연" : all_actor
# }
# dat = pd.DataFrame(dat_dict)
# dat.to_csv("네이버영화.csv", index=False)
# dat.to_excel("네이버영화.xlsx", index=False)