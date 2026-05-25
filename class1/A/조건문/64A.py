# 064A -> 세 개의 정수를 이어붙여서 하나의 정수로 만들었을 경우 그것이 4의 배수인가?

r,g,b = input().split()

num = int(r+g+b)

if num%4 == 0:
    print('YES')
else:
    print('NO')