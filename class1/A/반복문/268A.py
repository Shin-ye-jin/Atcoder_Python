# 숫자 5개가 주어진다. 이 숫자들 중에 겹치지 않는 서로 다른 숫자가 총 몇 종류인지 알아내라.

nums = list(map(int, input().split()))
# 입력 31 9 24 31 24
unique_nums = []

for x in nums:
    if x not in unique_nums:
       unique_nums.append(x)

print(len(unique_nums))
