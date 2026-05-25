# 176A -> N개를 만들어줘야 한다. 한 번에 X개를 만들 수 있다. 그걸 만드는데 T시간이 걸린다.

# N X T (20 12 6)

n,x,t = map(int,input().split())

res = 0

while True:
    n -= x

    res += t

    if n < 0:
        break

print(res)