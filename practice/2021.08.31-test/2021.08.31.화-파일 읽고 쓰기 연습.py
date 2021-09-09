# 파일열기
var = open('test01.txt', 'w', encoding ='utf-8')

# 손님의 이름, 나이, 성별 입력받기
name = input("이름을 입력해주세요. : ")
age = input("나이를 입력해주세요. : ")
gen = input('성별을 입력해주세요. : ')

# 손님의 정보 파일에 기록하기
var.write(name + ',' + age + ',' + gen)
# 기록된 파일 출력하기
var.close()
