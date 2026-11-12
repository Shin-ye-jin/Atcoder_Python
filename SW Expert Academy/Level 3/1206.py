# 1206 [S/W 문제해결 기본] 1일차 - View

for num in range(10):
    n = int(input())
    matrix = list(map(int,input().split()))

    count = 0

    for i in range(2,n-2):
        left_side = max(matrix[i-2],matrix[i-1])
        right_side = max(matrix[i+1],matrix[i+2])

        max_side = max(left_side,right_side)

        if matrix[i] > max_side:
            count = count + (matrix[i] - max_side)

    print(f"#{num+1} {count}")