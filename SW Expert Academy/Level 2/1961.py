# 1961 숫자 배열 회전

n = int(input())

matrix = [list(map(int,input().split())) for _ in range(n)]
result = [[0 for _ in range(n)] for _ in range(n)]

for w in range(n):
    for i in range(n):
        for j in range(n):
            if (i+n-1) > n-1:
                m = (i+n-1)%(n-1)
                result[j][m] = matrix[i][j]
            else:
                m = i + n-1
                result[j][m] = matrix[i][j]
    print(matrix)

# print(matrix)