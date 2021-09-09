from bs4 import BeautifulSoup

page = '''
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
soup = BeautifulSoup(page, "html.parser")
b = soup.body
# print(b)
b1 = soup.body.children
# print(b1)
# >>> <list_iterator object at 0x000001B5043A7100> 정상적으로 처리됨.
# print(list(b1))
# 줄 바꿈 태그("\n")와 태그 내용이 각각 요소로 담기는 리스트 출력.

# [영역2] 출력
# [영역2]가 담긴 태그만 가져오기
b2 = list(b1)
print(b2[-2])
print(len(b2))

# p 태그만 가져오기
b3 = b2[-2]
b4 = b3.find_all("p")
print(b4)

# 텍스트만 출력
for i in b4:
	print(i.text)

print("==========최종 정리==========")
# 정리
body_sort = list(soup.body.children)[-2].find_all("p")
for one in body_sort:
	print(one.text)