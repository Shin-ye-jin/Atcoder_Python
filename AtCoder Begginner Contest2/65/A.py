# A - Expired?

import sys

x,a,b = map(int,sys.stdin.readline().split())

if a >= b:
    print('delicious')
elif a < b:
    if b-a >= x+1:
        print('dangerous')
    else:
        print('safe')
