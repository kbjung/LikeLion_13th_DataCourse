import requests
from bs4 import BeautifulSoup
from datetime import datetime

url = "http://www.daum.net"
response = requests.get(url)

# print(type(response.text)) 결과 "str"
soup = BeautifulSoup(response.text, "html.parser")

# print(soup)

#====================================================================
# file = open("daum.html","w") daum.html 파일을 열거나 만들고, 덮어쓰기
# file.write(response.text) file에 response.text를 기록
# file.close() file 닫기
#================= 동일한 결과 ========================================
# with open("daum.html", "w") as file:
#     com_file = file.write(response.text)
#====================================================================

# print(soup.title) title tag 맨윗줄 1개만
# print(soup.title.string) title tag 중 tag제외 문자만
# print(soup.span) span tag 맨윗줄 1개만 
# print(soup.findAll("span")) spna tag 전부

results = soup.findAll("a", "link_favorsch")
# a 와 link_favorsch tag가 있는 모든 tag를 results에 리스트로 저장
# print(results) 결과 긴 리스트

print(datetime.today().strftime("%Y년 %m월 %d일의 실시간 검색어 순위입니다. \n"))

rank = 1
for result in results:
    print(rank, "위 :",result.get_text(),"\n")
    rank += 1
#result.get_text() : result에서 텍스트만