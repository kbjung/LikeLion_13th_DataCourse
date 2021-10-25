# 4-3 module02.py를 만들어보기(좌, 우 움직임-함수)

# 모듈 이름 : module02
# 기능
#  왼쪽으로 이동
#  오른쪽으로 이동
import module01

loc = module01.loc # loc : 리스트

def left_move():
    loc[0] -= 1
    print('좌측으로')
    print(f'현재 위치 : X = {loc[0]}, Y = {loc[1]}')

def right_move():
    loc[0] += 1
    print('우측으로')
    print(f'현재 위치 : X = {loc[0]}, Y = {loc[1]}')
