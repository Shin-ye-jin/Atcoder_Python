# A - Grouping

import sys

a = [1, 3, 5, 7, 8, 10, 12]
b = [4, 6, 9, 11]
c = [2]

x,y = map(int,sys.stdin.read().split())
# 시간 초과? 런타임 오류가 나서 변경함

if x in a:
    if y in a:
        print('Yes')
    else:
        print('No')
elif x in b:
    if y in b:
        print('Yes')
    else:
        print('No')
elif x in c:
    if y in c:
        print('Yes')
    else:
        print('No')
else:
    print('No')

