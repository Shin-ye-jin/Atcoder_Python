# 1961 숫자 배열 회전

n = int(input())

for w in range(1, n+1):
    m = int(input())
    matrix = [list(map(int,input().split())) for _ in range(m)]

    print(f"#{w}")

    for i in range(m):
        w90 = ""
        for j in range(m-1,-1,-1):
            w90 += str(matrix[j][i])

        w180 = ""
        for j in range(m-1,-1,-1):
            w180 += str(matrix[m-1-i][j])

        w270 = ""
        for j in range(m):
            w270 += str(matrix[j][m-1-i])

        print(f"{w90} {w180} {w270}")


# matrix = [list(map(int,input().split())) for _ in range(n)]
# # result = [[0 for _ in range(n)] for _ in range(n)]
# result1 = [[] for _ in range(n)]
# for i in range(n):
#     tmp=""
#     for j in range(n-1,-1,-1):
#         tmp +=str(matrix[j][i])
#     result[i][0] = tmp
#
#
#
# print(result)
# for w in range(n):
#     for i in range(n):
#         for j in range(n):
#             if (i+n-1) > n-1:
#                 m = (i+n-1)%(n-1)
#                 result[j][m] = matrix[i][j]
#             else:
#                 m = i + n-1
#                 result[j][m] = matrix[i][j]
#     print(matrix)

# print(matrix)