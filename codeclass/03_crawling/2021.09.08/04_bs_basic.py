from urllib.request import urlopen
from bs4 import BeautifulSoup

# url = "https://finance.naver.com/"
# page = urlopen(url) # 웹 URL로부터 페이지를 가져오기
# print(page)

page = '''
<html>
<title>나의 홈페이지</title>
<body>
<div>
<a href="https://www.naver.com/">naver</a>
<a href="https://www.google.com">google</a>
<img height="300" src="dog_01.jpg" width="500"/>
<p> 내가 가장 좋아하는 동물은 강아지입니다.</p>
<p> 나는 그리고 네이버 홈페이지에 자주 갑니다.</p>
<p class="p3"> 강아지 사진과 네이버 링크 </p>
<p id="p4"> 간단한 나의 홈페이지를 만들다.</p>
<p class="p3"> 강아지 사진과 네이버 링크222 </p>
</div>
</body>
</html>
'''

# html parse
soup = BeautifulSoup(page, 'lxml')
print(soup.title)

# 태그명 soup.태그명 => 해당 요소의 정보를 가져온다.(맨 윗줄 하나)
# print(soup.title)
# print(soup.body)
# print(soup.div)
# print(soup.img)
print(soup.a)
print(soup.a.text)
print(soup.div.p.text)

# id, class 를 활용해서 정보 가져오기 - 하나의 요소(find)
# id, class 를 활용해서 정보 가져오기 - 모든 요소(find_all)
print(soup.find(id="p4"))
print(soup.find_all("p"))

# find, find_all
# 2-2 실습하기 - naver와 모든 a태그 요소 가져오기
# naver 정보
# 모든 a태그 정보 가져오기
print(soup.find("a").text)
print(soup.find_all("a")) # 타입 : BS의 리스트 형태

# 2-2 (추가) div 요소 정보를 가지고 온 후, p(id="p4")요소 가져오기 - 댓글달기
# my sol1.
div = soup.div
print(div.find("p",id="p4"))

# my sol2.
print(soup.div.find("p",id="p4"))

# 2-3 실습해보기
# 한줄 코드
# class 정보를 이용해서 p3인 것을 가져와서 2번째 요소의 text를 가져오기.

# my sol1.
p = soup.find_all(class_="p3")
# print(p)
print(p[1].text)

# sol.
print(soup.find_all(class_="p3")[1].text)

# 2-3 (추가) a태그의 link 정보 가져오기
# my sol.
links = soup.find_all("a")
print(links[0]["href"])

# sol.


# 2-4 실습해 보기 google 텍스트 정보 가져오기
# my sol.
print(soup.find_all("a")[1].text)