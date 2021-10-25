from bs4 import BeautifulSoup
from urllib.request import urlopen

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

soup = BeautifulSoup(page, 'lxml') # html.parser, html5lib, lxml(anaconda)

# title 요소 정보 가져오기
print(soup.title)

# a 태그 요소 가져오기(첫 번째 줄만)
print(soup.a)

# a 태그 요소 가져오기
print(soup.find_all("a"))

# 7-2 (추가) p태그 전체 가져오기
print(soup.find_all("p"))

# 7-2 (추가) p태그의 id가 p4인 요소 가져오기
print(soup.find(id="p4"))