# 4달러 도넛과 7달러 도넛이 있다. n달러 돈 내에서 정확하게 구입할 수 있는 방법을 구해라.

n = int(input()) # 11 입력
ans = "No"

for cake in range(26):
   for donut in range(26):
      total = (4*cake) + (7*donut)

      if total == n:
         ans = "Yes"
         break

print(ans)