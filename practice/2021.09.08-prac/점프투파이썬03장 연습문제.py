# Q1. 다음 코드의 결과값은?
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
# A1. : shirt 출력

# Q2. while문을 사용해 1부터 1000까지의 자연수 중 3의 배수의 합을 구해 보자.
# sol2 :
i = 0
sum = 0
while i <= 1000:
	if i % 3 ==0:
		sum += i
	i += 1
print(sum) # 166833 출력

# A2. :
# result = 0
# i = 1
# while i <= 1000:
#     if i % 3 == 0: # 3으로 나누어 떨어지는 수는 3의 배수
#         result += i
#     i += 1
#
# print(result) # 166833 출력



# Q3. while문을 사용하여 다음과 같이 별(*)을 표시하는 프로그램을 작성해 보자.
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

# A3. :
# i = 0
# while True:
#     i += 1 # while문 수행 시 1씩 증가
#     if i > 5: break     # i 값이 5보다 크면 while문을 벗어난다.
#     print('*' * i)     # i 값 개수만큼 *를 출력한다.

# Q4. for문을 사용해 1부터 100까지의 숫자를 출력해 보자.

# sol
for i in range(1,101):
	print(i)

# Q5.
# A 학급에 총 10명의 학생이 있다. 이 학생들의 중간고사 점수는 다음과 같다.
#
# [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
#
# for문을 사용하여 A 학급의 평균 점수를 구해 보자.

n = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
s = 0
for i in n:
	s += i

print("A학급의 평균 :", s/len(n))

# Q6.
# 리스트 중에서 홀수에만 2를 곱하여 저장하는 다음 코드가 있다.
#
# numbers = [1, 2, 3, 4, 5]
# result = []
# for n in numbers:
#     if n % 2 == 1:
#         result.append(n*2)
# 위 코드를 리스트 내포(list comprehension)를 사용하여 표현해 보자.

# A6.
# 리스트 내포로 표현하면 다음과 같다.

numbers = [1, 2, 3, 4, 5]
result = [n*2 for n in numbers if n%2==1]
print(result)
# [2, 6, 10]