# 1979 어디에 단어가 들어갈 수 있을까

temp = int(input())

for w in range(temp):
    n, k = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(n)]
    result = 0

    for i in range(n):
        count = 0
        for j in range(n):
            if matrix[i][j]== 1:
                count+=1
            else:
                if count == k:
                    result += 1
                count=0
        if count == k:
            result += 1

    for j in range(n):
        count = 0
        for i in range(n):
            if matrix[i][j]== 1:
                count+=1
            else:
                if count == k:
                    result += 1
                count = 0
        if count == k:
            result += 1


    print(f"#{w+1} {result}")


# for i in range(n):
#     count = 1
#     for j in range(1,n):
#         if matrix[i][j-1] == 1 and matrix[i][j] == 1:
#             count+=1
#     print(count)
#     if count == k:
#         result += 1
#
# # print(result)
#
# for j in range(n):
#     count = 1
#     for i in range(1,n):
#         if matrix[i-1][j] == 1 and matrix[i][j] == 1:
#             count+=1
#     if count == k:
#         result += 1
#
# # print(result)