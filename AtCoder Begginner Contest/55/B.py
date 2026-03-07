# B - Training Camp
# 처음 파워 : 1
# 1번째 운동 후 : 1*1 = 1
# 2번째 운동 후 : 1*2 = 2
# 3번째 운동 후 : 2*3 = 6
# 4번째 운동 후 : 6*4 = 24
# N번째 운동 후 : (n-1번째까지의 파워)*n
import sys

n = int(sys.stdin.readline()) # 시간 초과 문제를 대비해서
res = 1
nod = 10**9 + 7
for i in range(1,n+1):
    res = (res*i)%nod # 시간 초과 문제를 대비해서

print(res)