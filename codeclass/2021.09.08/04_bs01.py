from bs4 import BeautifulSoup

page1 = '''
<html>
<title>나의 홈페이지</title>
<body>

<div>
    
</div>

<div>
    
</div>

<div>
    <a href="https://www.naver.com/">naver</a>
    <a href="https://www.google.com">google</a>
    <p class="p3"> [영역1] 필요없는 정보1 </p>
    <p class="p3"> [영역1] 필요없는 정보3 </p>
    <p id="p4"> [영역1] 필요없는 정보2 </p>
</div>
<div>
    <a href="https://www.naver.com/">naver</a>
    <a href="https://www.google.com">google</a>
    <p class="p3"> [영역2] 강아지 사진과 네이버 링크 </p>
    <p class="p3"> [영역2] 강아지 사진과 네이버 링크222 </p>
    <p id="p4"> [영역2] 간단한 나의 홈페이지를 만들다.</p>
</div>
</body>
</html>
'''

#
soup1 = BeautifulSoup(page1, 'lxml')
# print( soup1.title )

#
# one_info = soup1.find_all("div")
# print(len(one_info))
# print(one_info[3])

# wanted_info = soup1.find_all('div')[3]
# print(wanted_info)
# last_info_multi = wanted_info.find_all('p', class_="p3")
# print(last_info_multi)
#
# for one in last_info_multi:
# 	print(one.text)

# 3-3 (추가) 아래 정보 가져오기
#     <p class="p3"> [영역1] 필요없는 정보1 </p>
#     <p class="p3"> [영역1] 필요없는 정보3 </p>
# sol.
wanted_info = soup1.find_all('div')[2]
print(wanted_info)
last_info_multi = wanted_info.find_all('p', class_="p3")
print(last_info_multi)

for one in last_info_multi:
	print(one.text)


# 3-3 (추가) 이를 우리가 원하는 리스트에 담아보기 - 댓글 달기
# # my sol1.
# div2 = soup1.find_all('div')[2]
# want_div2 = div2.find_all(class_="p3")
# list1 = []
# for i in want_div2:
# 	list1.append(i.text)
# print(list1)

# sol.
a = []
for one in last_info_multi:
	a.append(one.text)

# children : 자기자신의 태그 제외하고 나머지 태그 리스트 형태로 가져온다.
wanted_info = soup1.find_all('div')[2]
print(wanted_info.children) # div 태그의 한 단계 낮은 태그들을 리스트로 모음.
print(list(wanted_info.children)[9])

