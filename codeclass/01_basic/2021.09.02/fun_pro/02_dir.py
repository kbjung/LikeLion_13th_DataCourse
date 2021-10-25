# dir() : 객체가 자체적으로 가지고 있는 변수나 함수(메서드)를 보여준다.
a = [1, 2, 3]
print(dir(a))

# enumerate() : 순서가 있는 자료형(리스트, 튜플, 문자열)을 입력받아 인덱스 값을 포함하는 enumerate객체를 돌려준다.
a = ['a', 'b', 'c']
print(enumerate(a))
print(list(enumerate(a)))

# turple
t = (1, 2, 3)
print(t)