# 165A -> K의 배수가 A와 B 사이에 있는가? 달성할 수 있다면 OK, 없다면 NG

# K A B ( 7 500 600)

k = int(input())

a,b = map(int,input().split())

num = a//k+1

if num*k <= b:
    print("OK")
else:
    print("NG")