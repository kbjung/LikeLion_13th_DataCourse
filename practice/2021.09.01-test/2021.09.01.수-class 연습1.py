# 사칙연산 계산기

# 덧셈 계산기
def add(a, b):
    return print("{} + {} = {}".format(a, b, a+b))
# 뺄셈 계산기
def min(a, b):
    return print("{} - {} = {}".format(a, b, a-b))
# 곱셈 계산기
def mul(a, b):
    return print("{} X {} = {}".format(a, b, a*b))
# 나눗셈 계산기
def div(a, b):
    return print("{} / {} = {}".format(a, b, a/b))

num1 = int(input("계산할 첫번째 값을 입력하세요. : "))
num2 = int(input("계산할 두번째 값을 입력하세요. : "))
add(num1, num2)
min(num1, num2)
mul(num1, num2)
div(num1, num2)

# 클래스 이용 사칙연산 계산기
# 각각 입력 받은 값에 대해 계산
# (단점)동일한 값에 대해 여러 연산 하려면 매써드에 동일한 값 입력해야함.

class Cal:
    result = 0
    # 덧셈 계산기
    def add(self, a, b):
        self.result = a + b
        return print(self.result)
    # 뺄셈 계산기
    def min(self, a, b):
        self.result = a - b
        return print(self.result)
    # 곱셈 계산기
    def mul(self, a, b):
        self.result = a * b
        return print(self.result)
    # 나눗셈 계산기
    def div(self, a, b):
        self.result = a / b
        return print(self.result)

c1 = Cal()
c1.add(2, 3)
c1.min(3, 5)
c1.mul(2, 5)
c1.div(3, 6)
print()

# 매써드 오버라이딩(method overriding)
# 0으로 나눌 때 메세지 출력
class Cal2(Cal):
    def div(self, a, b):
        if b == 0:
            print("0으로 나눌 수 없습니다.")
        else:
            return print(a/b)

c2 = Cal2()
c2.div(4, 0)
c2.div(4, 2)