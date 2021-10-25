# abs() : 절대값 함수
print(abs(3))
print(abs(-13))

# 6-2 실습 - 두 개의 값을 입력받아서, 값의 차이의 절대값를 구하는 프로그램을 만들어보자.

# 차의 절대값 구하는 함수
def fun(a, b):
    result = a - b
    return abs(result)

# 두개의 값을 입력 받기
num1 = int(input("첫 번째 값을 입력하세요 : "))
num2 = int(input("첫 번째 값을 입력하세요 : "))

# 차의 절대값 출력
print(fun(num1, num2))