# 1부터 N까지 숫자 중에 홀수가 몇 개인가?

N = int(input())
odd = 0

for i in range(1, N+1):
    if i % 2 != 0:
       odd += 1

print(odd / N)