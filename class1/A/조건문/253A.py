# 세 숫자가 a,b,c가 주어진다. 가운데 있는 숫자 B가 세 수 중에서 정확히 ‘중간값’인지 판별하라

a, b, c = map(int,input().split())
# a 5, b 3, c 2

if a<=b<=c or c<=b<=a:
    print("Yes")
else:
    print("No")
