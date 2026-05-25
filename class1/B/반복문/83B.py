# 083A -> 저울이 왼쪽으로 기울어진다면 Left / 균형이 맞다면 Balanced / 오른쪽 끝이라면 Right

# A B C D (3 8 7 1)

a,b,c,d = map(int,input().split())

n1 = a+b

n2 = c+d

if n1 > n2:
    print("Left")
elif n1 == n2:
    print("Balanced")
else:
    print("Right")