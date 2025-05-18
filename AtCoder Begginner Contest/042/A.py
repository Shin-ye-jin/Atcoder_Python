# Iroha and Haiku (ABC Edition)
matrix = list(map(int,input().split()))

if matrix.count(5) == 2:
    if matrix.count(7) == 1:
        print("YES")
    else:
        print("NO")
else:
    print("NO")