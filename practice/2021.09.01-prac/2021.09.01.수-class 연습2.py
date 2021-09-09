# 사칙연산 계산기
# class에서 self, first, second 이용
# 입력 받은 값에 대한 여러 계산 한번에 처리
# (단점)다른 값에 대한 계산 하려면 class에 값 다시 입력 해야함.

class Cal:
    # 생성자(constructor) 설정
    def __init__(s, a, b):
        s.a = a
        s.b = b
    def add(s):
        return s.a + s.b
    def min(s):
        return s.a - s.b
    def mul(s):
        return s.a * s.b
    def div(s):
        return s.a / s.b

c1 = Cal(2, 4)
print(c1.add())
print(c1.min())
print(c1.mul())
print(c1.div())

class Cal2(Cal):
    def div(s):
        if s.b == 0:
            print("0으로 나눌 수 없습니다.")
        else:
            return s.a / s.b

c2 = Cal2(4, 0)
print(c2.add())
print(c2.min())
print(c2.mul())
print(c2.div())