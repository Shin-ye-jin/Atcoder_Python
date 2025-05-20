# C - Iroha's Obsession
n,k = map(int,input().split())
d = list(map(int,input().split()))

n = str(n)
n = list(n)

while True:
    f = True
    for i in range(k):
        if str(d[i]) in n:
            f = False
    if f:
        print("".join(n))
        exit()
    else:
        n = int("".join(n))+1
        n = list(str(n))

# n의 숫자에 d의 숫자들이 포함되었는가! 포함되지 않을 때까지 1씩 더함

