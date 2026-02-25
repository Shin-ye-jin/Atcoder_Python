# B - Problem Statement
# N : 문제 수
# Ti : 각 문제 해결을 위한 필요한 초
# M : 참가자들에게 제공되는 음료 종류(딱 한 종류만 가능)
# Pi : 그녀의 뇌가 자극을 받아 문제를 해결하는 데 걸리는 시간
# xi: ,,?

# 3
# 2 1 4
# 2
# 1 1
# 2 3
# 뭔말인가 했다. 1번 문제의 걸리는 시간을 1로 바꾸기
# 2번 문제의 걸리는 시간을 3으로 바꾸기

n = int(input())
t = list(map(int,input().split()))
m = int(input())

s = sum(t)

for i in range(m):
    a,b = map(int,input().split())
    res = s - t[a-1] + b
    print(res)
