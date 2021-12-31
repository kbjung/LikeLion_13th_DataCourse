#dictionary
dic = {"사는 곳" : "서울", "취미" : "운동"}
print(dic)
#{ key : value, key : value}
#{"사는 곳" : "서울", "취미" : "운동"}

#dictionary에 원소 추가
dic["좋아하는 음식"] = "국수"
print(dic)

#dictionary의 value 값 교체하기
dic["취미"] = "독서"
print(dic)

#dictionary의 값 삭제하기
del dic["좋아하는 음식"]
print(dic)

#dictionary를 완전히 비우기
dic.clear()
print(dic)


#dictionary
dic = {"사는 곳" : "서울", "취미" : "운동"}

# dic의 key값만 출력하기
print(dic.keys())

# dic의 value 값만 출력하기
print(dic.values())

# dic의 key값과 value값 모두 출력하기
print(dic.items())