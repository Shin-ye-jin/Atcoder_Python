# 숫자 N이 주어지고, 그 다음 줄에 숫자 N개가 주어진다. for문을 N번 돌면서 입력되는 숫자들을 변수에 더해 총합을 출력해라.

n = int(input()) # 3 입력
numbers = map(int, input().split())
# 2 7 2 입력
total = 0

for num in numbers:
     total += num

print(total)