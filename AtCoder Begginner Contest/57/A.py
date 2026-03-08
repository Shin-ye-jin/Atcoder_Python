# a - Remaining Time
# 파파고 번역!!! 현재 시간 A에서 B 시간 지난 후
a,b=map(int,input().split())

res = a+b

if res > 23:
    print(res%24)
else:
    print(res)
