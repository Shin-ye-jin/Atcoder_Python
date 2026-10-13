# 1974 스도쿠 검증

matrix = [list(map(int,input().split())) for _ in range(9)]


# 행
for row in matrix:
    count_box = [0] * 10
    for val in row:
        count_box[val] += 1
    for i in range(1,10):
        if count_box[i] != 1:
            print(i,0)
            break
# 열
for j in range(9):
    count_box = [0]*10
    for i in range(9):
        m = matrix[i][j]
        count_box[m] += 1
    for x in range(1,10):
        if count_box[x] != 1:
            print(x,0)
            break