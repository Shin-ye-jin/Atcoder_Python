# 다리 높이가 N개 주어진다. 제시된 다리 높이 중 가장 높은게 몇 번째인지 출력하시오.

n = int(input()) # 3
a, b, c = map(int,input().split())
# A 50 B 80 C 70

if a >= b and a >= c:
   print(1)
elif b >= a and b >= c:
   print(2)
else:
   print(3)

# ans = arr.index(max_value) + 1