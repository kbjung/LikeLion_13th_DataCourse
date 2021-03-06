# 1.홍길동 씨의 과목별 점수는 다음과 같다. 홍길동 씨의 평균 점수를 구해 보자.
# *과목	점수
# *국어	80
# *영어	75
# *수학	55

mean = ( 80 + 75 + 55 ) / 3
print(mean)

# 2.자연수 13이 홀수인지 짝수인지 판별할 수 있는 방법에 대해 말해 보자.

n = 13
if n % 2 == 0 :
    print("13은 짝수입니다.")
else:
    print("13은 홀수입니다.")

# 3. 홍길동 씨의 주민등록번호는 881120-1068234이다. 홍길동 씨의 주민등록번호를 연월일(YYYYMMDD) 
# 부분과 그 뒤의 숫자 부분으로 나누어 출력해 보자.
# ※ 문자열 슬라이싱 기법을 사용해 보자.

w = "881120-1068234"
print(w[:6], w[7:])

# 4. 주민등록번호 뒷자리의 맨 첫 번째 숫자는 성별을 나타낸다. 주민등록번호에서 성별을 나타내는 숫자를 출력해 보자.
# ※ 문자열 인덱싱을 사용해 보자.
# pin = "881120-1068234"

pin = "881120-1068234"
print(pin[7])

# 5. 다음과 같은 문자열 a:b:c:d가 있다. 문자열의 replace 함수를 사용하여 a#b#c#d로 바꿔서 출력해 보자.
#  a = "a:b:c:d"

a = "a:b:c:d"
print(a.replace(":", "#"))

# 6. [1, 3, 5, 4, 2] 리스트를 [5, 4, 3, 2, 1]로 만들어 보자.
# ※ 리스트의 내장 함수를 사용해 보자.

li = [1, 3, 5, 4, 2]
li.sort(reverse = True)
print(li)

# 7. ['Life', 'is', 'too', 'short'] 리스트를 Life is too short 문자열로 만들어 출력해 보자.
lis= ['Life', 'is', 'too', 'short']
for i in lis:
    print(i, end = " ")
print("")

# 8. (1,2,3) 튜플에 값 4를 추가하여 (1,2,3,4)를 만들어 출력해 보자.
# ※ 더하기(+)를 사용해 보자.
t = (1,2,3)
t1 = (4,)
t2 = t + t1
print(t2)

# 9. 다음과 같은 딕셔너리 a가 있다.
# >>> a = dict()
# >>> a
# {}
# 다음 중 오류가 발생하는 경우를 고르고, 그 이유를 설명해 보자.
# 1. a['name'] = 'python'
# 2. a[('a',)] = 'python'
# 3. a[[1]] = 'python'
# 4. a[250] = 'python'

a = dict()
a['name'] = 'python'
print(a)

a = dict()
a[('a',)] = 'python'
print(a)

# 오류 발생 : key 값이 리스트형이라 타입 에러 발생
# a = dict()
# a[[1]] = 'python'
# print(a)

a = dict()
a[250] = 'python'
print(a)

# 10. 딕셔너리 a에서 'B'에 해당되는 값을 추출해 보자.
# >>> a = {'A':90, 'B':80, 'C':70}
# ※ 딕셔너리의 pop 함수를 사용해 보자.
a = {'A':90, 'B':80, 'C':70}
print(a.pop("B"))

# 11. a 리스트에서 중복 숫자를 제거해 보자.
# >>> a = [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5]
# ※ 집합 자료형의 요솟값이 중복될 수 없다는 특징을 사용해 보자.
a = [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5]
set_a = set(a)
list_a = list(set_a)
print(list_a)

# 12. 파이썬은 다음처럼 동일한 값에 여러 개의 변수를 선언할 수 있다. 다음과 같이 a, b 변수를 선언한 후 
# a의 두 번째 요솟값을 변경하면 b 값은 어떻게 될까? 그리고 이런 결과가 오는 이유에 대해 설명해 보자.
# >>> a = b = [1, 2, 3]
# >>> a[1] = 4
# >>> print(b)

# => [1, 2, 3]이 출력된다. 리스트 a의 두번째 요소만 변한거라 리스트 b에는 영향없다.(X)
a = b = [1, 2, 3]
a[1] = 4
print(b)
# 정답 : [1, 4, 3], a와 b는 모두 리스트 [1, 2, 3]을 가리키기 때문이다.