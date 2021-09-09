### mydream.py 모듈 이용하는 파일

import mydream

print("내가 좋아하는 색깔은 :", mydream.likecolor)
myact1 = mydream.myact()
myact2 = mydream.myact()

# 5-3 (추가) 오늘의 행동을 추가(myact1, myact2) 두가지 행동하기
print("내가 좋아하는 운동은",myact1.run())
print("힘들 때는", myact2.play())

