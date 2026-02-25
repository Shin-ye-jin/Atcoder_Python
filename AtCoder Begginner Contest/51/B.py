# B - Sum of Three Integers
# x,y,z가 각각은 k보다는 작거나 같아야 함.
# x+y+z는 s랑 같아야 한다.

# k,s = map(int,input().split())
#
# sum = 0
#
# for x in range(k+1):
#     for y in range(k+1):
#         for z in range(k+1):
#             if x+y+z == s:
#                 sum+=1
#
# print(sum)
# 답은 맞으나 시간초과가 남

import sys
k,s = map(int, sys.stdin.readline().split())

res = 0

for x in range(k+1):
    for y in range(k + 1):
        z = s - x - y

        if 0<=z<=k:
            res+=1
print(res)

# 기존 코드는 k = 2500일 때, 2501 * 2501 * 2501
# 수정 코드는 k = 2500일 때, 2501 * 2501 번 연산