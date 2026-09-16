# 1954 달팽이 숫자

# 방향 벡터
# 우->하->좌->상 순서로 방향 벡터를 정의하고
# 벽에 부딪히거나 이미 숫자가 채워진 칸을 만나면 방향 전환

dr = [0,1,0,-1]
dc = [1,0,-1,0]

num = int(input())

for x in range(num):

    n = int(input())

    matrix = [[0]*n for _ in range(n)]

    r,c,dist = 0,0,0

    for i in range(1,n*n+1):
        matrix[r][c] = i
        nr = r + dr[dist % 4]
        nc = c + dc[dist % 4]

        if nr < 0 or nr >= n or nc <0 or nc >= n or matrix[nr][nc] != 0:
            dist += 1
            nr = r + dr[dist % 4]
            nc = c + dc[dist % 4]

        r,c = nr, nc
    print(f"#{x+1}")
    for row in matrix:
        print(" ".join(map(str, row)))
