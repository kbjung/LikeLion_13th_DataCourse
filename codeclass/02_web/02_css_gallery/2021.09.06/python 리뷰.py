### 리스트
a1 = [1, 2, 3, 4]
a2 = [11, 21, 31, 41]

### 딕셔너리
b = {'key1':[1, 2, 3], 'key2':['a','b']}

### 리스트 인덱싱, 슬라이싱
print(a1[2])
print(a2[1:2])

### 리스트와 튜플의 차이
### 튜플은 수정, 변경, 추가가 안된다.

### 리스트 '+'
print(a1 + a2)
	# 두 리스트가 하나의 리스트로 합쳐져서 출력

### 자료의 요소의 개수, 문자열의 길이구하기
print(len(a1))
print(del a1[1])
print(a1)

### 집합 자료형
c = []
if c:
	print('True')
else:
	print('False')
	# 결과 : False

a = [1, 2, 3, 4]
for idx, val in enumerate(a):
	print(idx, val)

b = ['a', 'b', 'c', 'd']
if 'a' in b:
	print("True")
else:
	print("False")

for i in range(0, 10, 1):
	if i%2 == 0:
		continue
	print(i)
	# 홀수 출력

for i in range(0, 10, 1):
	if i%2 == 0:
		break
	print(i)
	# 출력없이 종료

def plus():
	print("return")
	return 999

rusult_num = plus()
if result_num == 999:
	print("정상실행")

### 지역변수와 전역변수
# 지역변수 : 함수 내에 선언된 변수
# 전역변수 : 함수 바깥, 코드에 선언된 변수
# 전역 변수를 함수 내에서도 적용하려면 "global 전역변수명" 입력

def plus(num1, num2 = 0):
	result = num1 + num2
	return result

plus(3)

### open() : 파일 열기 시작
### 파일 모드 : r, w, a
### 이미지 파일 읽기 : rb
### 이미지 파일 쓰기 : wb
### 텍스트 파일 읽기
### read(), read(size)
### readline()
### readlines()
### 클래스 선언 : class
### 클래스
class Cal:
	pass

### 클래스 상속
class Cal_Up(Cal):
	pass

### 생성자 메써드(constructor)
def __init__(self):
	pass

### 프로그램 실행
# 01 python __.py => __name__ => __main__
# 02 import __    => __name__ => 모듈명
# 내부 변수 : __name__
# if __name__= "__main__":

### 모듈
### 클래스, 모듈, 함수, 라이브러리
### 라이브러리 > 모듈 > 클래스 > 함수

### 예외처리
### try:
###		실행문1
###	except:
###		실행문2