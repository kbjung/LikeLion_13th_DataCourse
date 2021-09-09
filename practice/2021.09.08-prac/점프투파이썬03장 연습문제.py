# Q1 다음 코드의 결과값은?
a = "Life is too short, you need python"

if "wife" in a:
	print("wife")
elif "python" in a and "you" not in a:
	print("python")
elif "shirt" not in a:
	print("shirt")
elif "need" in a:
	print("need")
else:
	print("none")

# sol1 : python과 need 출력(X)
# A1 : shirt 출력

# Q2 while문을 사용해 1부터 1000까지의 자연수 중 3의 배수의 합을 구해 보자.
# sol2 :
i = 0
sum = 0
while i <= 1000:
	if i % 3 ==0:
		sum += i
	i += 1
print(sum) # 166833 출력

# A2 :
# result = 0
# i = 1
# while i <= 1000:
#     if i % 3 == 0: # 3으로 나누어 떨어지는 수는 3의 배수
#         result += i
#     i += 1
#
# print(result) # 166833 출력



# Q3 while문을 사용하여 다음과 같이 별(*)을 표시하는 프로그램을 작성해 보자.
# *
# **
# ***
# ****
# *****
# sol3 :
i = 0
while i < 5:
	print("*"*(i+1))
	i += 1

# A3 :
# i = 0
# while True:
#     i += 1 # while문 수행 시 1씩 증가
#     if i > 5: break     # i 값이 5보다 크면 while문을 벗어난다.
#     print('*' * i)     # i 값 개수만큼 *를 출력한다.
