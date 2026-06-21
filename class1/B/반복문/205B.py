# 리스트를 정렬하고 순열인지 아닌지 출력하라.

n = int(input()) # 5 입력
m = list(map(int,input().split()))
# 3 1 2 4 5 입력
count = 0
m.sort() # 오름차순 정렬

for i in range(1, n+1):
   if i not in m:
      count = 0
      break

if count == 0:
   print("Yes")
else:
   print("No")
