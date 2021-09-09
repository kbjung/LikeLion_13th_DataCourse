# 함수 연습
# 두 수를 입력받기
# 두 수의 합, 차, 곱, 나눗셈 출력

def two_make(a, b):
    return a + b, a - b, a * b, a / b
# return 여러값은 튜플로 저장됨.

# 두수를 입력 받기
a = int(input("첫번째 숫자를 입력하세요 : "))
b = int(input("두번째 숫자를 입력하세요 : "))
c = two_make(a, b)
d = ['합', '차', '곱', '나눗셈']
print(c)
print(type(c))
# 결과 출력
for i in range(4):
    print(f"입력한 {a}와 {b}의 {d[i]}은 {c[i]}입니다.")