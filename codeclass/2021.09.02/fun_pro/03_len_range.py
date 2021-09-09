a = ['a', 'b', 'c']
b = (1, 2, 3, 4)
c = "hello world"

print(len(a))
print(len(b))
print(len(c))

print(list(range(0, 10, 1)))

## isalpha() : 값 중에 알파펫이 있는가?
print('python'.isalpha())
print('p'.isalpha())

# 6-6 어떤 값또는 문자열을 입력받아서, 알파벳이 몇글자인지 확인해 보기
a = input("아무것이나 입력:")
cnt = 0

all_str =[]
for i in range(65, 91,1):
    all_str.append(chr(i))

for i in range(97, 123,1):
    all_str.append(chr(i))

print(all_str)
for one in a:
    if one in all_str:
        cnt += 1

print(f"알파벳은 {cnt}입니다.")

# 6-6 (추가) 알파벳, 공백, 숫자는 몇개인지...
a = input("아무것이나 입력:")
cnt = 0
c_num = 0
c_bl = 0

# 알파벳 리스트 만들기(ASCII 코드)
alp = []
for i in range(65, 91,1):
    alp.append(chr(i))

for i in range(97, 123,1):
    alp.append(chr(i))

# 숫자 리스트 만들기
num = []
for i in range(48, 58):
    num.append(chr(i))

# 알파벳, 숫자, 빈칸 개수 기록
for one in a:
    if one in alp:
        cnt += 1
    elif one in num:
        c_num += 1
    elif one == " ":
        c_bl += 1

print(f"알파벳은 {cnt}입니다.")
print(f"숫자는 {c_num}입니다.")
print(f"빈칸은 {c_bl}입니다.")