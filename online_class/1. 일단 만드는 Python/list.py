#list
list = [2, 3, 4, 5]
print(list)

#list에 원소 추가1(append) : 리스트 맨뒤에 추가
list.append(7)
print(list)

#list에 원소 추가2(insert) : 해당 index에 추가
list.insert(2, 9)
print(list)

#list의 원소 삭제하기(del)
del list[1]
print(list)

#list의 원소 삭제하기(.remove())
list.remove(4) # 처음 나오는 4를 삭제
print(list)

#list의 원소 부르기(index)
print(list[2])
print(list[-2])

#list의 원소 부르기(splicing)
print(list[2:])
print(list[:2])
print(list[-2:])
print(list[-3:-1])