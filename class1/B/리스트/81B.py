# 81B -> 입력받은 숫자가 전부다 짝수인가?

# N 3
# A1 A2 A3 (8 12 40)

n = int(input())

matrix = list(map(int,input().split()))

res = []

while True:
    for i in range(len(matrix)):
        if matrix[i] % 2 == 0:
            matrix[i] = matrix[i]//2