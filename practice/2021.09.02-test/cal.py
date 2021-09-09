# 사칙연산 계산기

class Cal:
    # 덧셈
    def add(s, a, b):
        s.a = a
        s.b = b
        return s.a + s.b
    # 뺄셈
    def min(s, a, b):
        s.a = a
        s.b = b
        return s.a - s.b
    # 곱셈
    def mul(s, a , b):
        s.a = a
        s.b = b
        return s.a * s.b
    # 나눗셈
    def div(s, a, b):
        s.a = a
        s.b = b
        if s.b == 0:
            print('0으로 나눌 수 없습니다.')
        else:
            return s.a / s.b

if __name__ == "__main__":
    print("cal.py를 직접 실행하셨습니다.")

# 터미널에서 python cal.py 입력하면 if문 실행
# 터미널에서 python 실행 후 import cal 입력하면 if문 실행X.