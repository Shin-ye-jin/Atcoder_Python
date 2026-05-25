a,b,c = map(int,input().split())
# 123 456 100 입력

n = 1
while True:
    if a <= c*n <= b:
        print(c*n)
        break
    elif c*n >b:
        print(-1)
        break
    n+=1