# A - 사탕을 둘러싼 싸움

a,b,c = map(int, input().split())

if a+b == c or a+c == b or b+c == a:
    print("Yes")
else:
    print("No")