# 숫자 3개가 주어짐. 이 숫자들을 크기 순서대로 나열했을 때, 이웃한 숫자들끼리의 간격이 똑같은지 판별하기

num = list(map(int, input().split()))

num.sort()

if num[1] - num[0] == num[2] - num[1]:
   print("Yes")
else:
   print("No")