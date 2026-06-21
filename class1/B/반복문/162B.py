# 숫자 n을 입력받고 n까지 숫자 중 3 또는 5의 배수에 해당하는 숫자를 제외하고 더한 총합을 출력하라.

n = int(input()) # 15 입력
sum = 0

for i in range(1,n+1):
    if n%3 == 0 or n%5==0:
      continue
    else:
      sum += i

print(sum)