# A부터 B까지 정수가 총 몇 개 있는지 for 문을 돌리면서 개수를 하나씩 세어 출력합니다.

a, b = map(int, input().split())
# 2 4 입력
count = 0

for i in range(a, b+1):
     count += 1

print(count)