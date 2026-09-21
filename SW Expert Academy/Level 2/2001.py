# 2001 파리 퇴치

tmp = int(input())

for x in range(1, tmp+1):
    n,m = map(int,input().split())

    matrix = [list(map(int,input().split())) for _ in range(n)]

    max_dead = 0

    for i in range(n-m+1):
        for j in range(n-m+1):
            c_sum = 0
            for r in range(m):
                for c in range(m):
                    c_sum += matrix[i+r][j+c]


            if c_sum > max_dead:
                max_dead = c_sum

    print(f"#{x} {max_dead}")
