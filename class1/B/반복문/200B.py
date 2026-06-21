# 정수 n과 k가 주어진다. 정확히 k번 반복한 후에 최종 n 값을 구하라.

n, k = map(int, input().split())
# 2021 4 입력

for i in range(k):
   if n%200 == 0:
      n = n//200
   else:
      n = int(str(n) + "200")

print(n)