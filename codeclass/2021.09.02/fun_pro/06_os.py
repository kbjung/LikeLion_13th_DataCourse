import os

# 현재 작업 위치
print(os.getcwd())

# 현재 작업 위치의 파일 보기
print(os.listdir())

# 7-2 (추가) 해당 위치의 파일이 몇개 있고, 그리고 원하는 파일이 있는지 확인 유무.
# 1. 해당 위치의 파일 개수
num = len(os.listdir())
print(f"현재 위치에 파일의 개수 : {num}")

# 2. 원하는 파일 있는지 확인
file = input("원하는 파일을 입력하세요 : ")
list = os.listdir()

if file in list:
    print(f"현재 위치에 {file}이 있습니다.")
else:
    print(f"현재 위치에 파일이 없습니다.")

# 7-3 (추가).py파일이 몇개인지.
count = 0
for i in list:
    if i[-3:] == ".py":
        count += 1

print(f".py 파일의 개수 : {count}")

# 참고 if ".py" in file: