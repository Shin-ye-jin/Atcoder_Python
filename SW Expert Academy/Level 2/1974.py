# 1974 스도쿠 검증

n = int(input())

for tmp in range(n):
    matrix = [list(map(int,input().split())) for _ in range(9)]
    result = 0

    for num in range(3):
        for w in range(3):
            count_box = [0] * 10
            for i in range(num*3,num*3+3):
                for j in range(w*3,w*3+3):
                    count_box[matrix[i][j]] += 1
            for number in range(1, 10):
                if count_box[number] != 1:
                    result += 1
                    break

    for row in matrix:
        count_box = [0] * 10
        for val in row:
            count_box[val] += 1
        for i in range(1,10):
            if count_box[i] != 1:
                result += 1
                break

    for j in range(9):
        count_box = [0]*10
        for i in range(9):
            m = matrix[i][j]
            count_box[m] += 1
        for x in range(1,10):
            if count_box[x] != 1:
                result += 1
                break

    if result == 0:
        print(f"#{tmp+1} {1}")
    else:
        print(f"#{tmp+1} {0}")

# 자.... 행 012하면서 열 012 345 678을 따로 봐야한다...

# for num in range(3):
#     for w in range(3):
#         for i in range(num * 3, num * 3 + 3):
#             count_box = [0] * 10
# 행 하나가 바뀔때마다 count_box가 0으로 리셋되어버림. 해서 w 밑으로 이동
#             for j in range(w * 3, w * 3 + 3):
#                 count_box[matrix[i][j]] += 1
#
#             for number in range(1, 10):  # <-- 이 루프 안쪽에 break가 있음
#                 if count_box[number] != 1:
#                     result += 1
#                     break
# 3*3(9칸)의 숫자를 세서 검사하고 싶다면 i와 j 이중 루프가 끝난 상태에서 검사

# for w in range(1,4):
#     for i in range(w*3-3,w*3):
#         for z in range(1,4):
#             count_box = [0] * 10
#             for j in range(z*3-3,z*3):
#                 print(matrix[i][j])
#                 count_box[matrix[i][j]] += 1
#             for v in range(1,10):
#                 if count_box[v] != 1:
#                     # print(v,0)
#                     break

# # 행
# for row in matrix:
#     count_box = [0] * 10
#     for val in row:
#         count_box[val] += 1
#     for i in range(1,10):
#         if count_box[i] != 1:
#             print(i,0)
#             break
# # 열
# for j in range(9):
#     count_box = [0]*10
#     for i in range(9):
#         m = matrix[i][j]
#         count_box[m] += 1
#     for x in range(1,10):
#         if count_box[x] != 1:
#             print(x,0)
#             break