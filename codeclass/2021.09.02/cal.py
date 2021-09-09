# 3-3 사칙연산 계산기 만들기
# 3-3 (추가) 계산기 클래스 만들기

# 사칙연산 계산기
class Cal:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def add(self):
        result = self.a + self.b
        print(f"{self.a} + {self.b} = {result}")
        return result
    def min(self):
        result = self.a - self.b
        print(f"{self.a} - {self.b} = {result}")
        return result
    def mul(self):
        result = self.a * self.b
        print(f"{self.a} * {self.b} = {result}")
        return result
    def div(self):
        result = self.a / self.b
        print(f"{self.a} / {self.b} = {result}")
        return result

# 계산기 업그레이드
class Cal2(Cal):
    def div(self):
        if self.b == 0:
            print("0으로 나눌 수 없습니다.")
        else:
            result = self.a / self.b
            print(f"{self.a} / {self.b} = {result}")
            return result
    # 제곱 계산
    def squ(self):
        result = self.a ** self.b
        print(f"{self.a} ** {self.b} = {result}")

# 두 값 입력 받기
num1 = int(input("첫 번째 값을 입력하세요. : "))
num2 = int(input('두 번째 값을 입력하세요. : '))

c2 = Cal2(num1, num2)
print()
c2.add()
c2.min()
c2.mul()
c2.div()
print()
c2.squ()
