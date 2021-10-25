####
####
#### 함수 < 클래스 < 모듈(함수, 변수, 클래스) < 라이브러리(패키지)

# 모듈 이름 : module01
# 기능
#  앞으로 이동
#  뒤로 이동

loc = [0, 0] # 현재 위치

def forward_move():
    loc[1] += 1
    print('앞으로')
    print(f'현재 위치 : X = {loc[0]}, Y = {loc[1]}')

def backward_move():
    loc[1] -= 1
    print('뒤로')
    print(f'현재 위치 : X = {loc[0]}, Y = {loc[1]}')
