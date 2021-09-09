# 문자열 포매팅 연습

# 문자열 포맷 코드
# 코드	설명
# %s	문자열(String)
# %c	문자 1개(character)
# %d	정수(Integer)
# %f	부동소수(floating-point)
# %o	8진수
# %x	16진수
# %%	Literal % (문자 % 자체)

a = "에이"
b = "비"
c = 3

# f-string
print(f"{a}와 {b}의 합은 {c}이다.")

# 숫자 바로 대입
print("1과 2의 합은 %d" %3)

# 문자열 바로 대입(%s)
print("지금은 %s 중 입니다." %"연습")

# 순서대로 포매팅
print('%s와 %s의 합은 %d이다.' %(a, b,  c))
print('{}와 {}의 합은 {}이다.'.format(a, b, c))

# 인덱스로 포매팅
print('{2}와 {1}의 합은 {0}이다.'.format(5, 3, 2))