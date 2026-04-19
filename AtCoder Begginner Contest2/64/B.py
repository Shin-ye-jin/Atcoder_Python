# B - Problem Statement

# 모든 집을 다 방문하려면, 가장 왼쪽 집투터 가장 오른쪽 집까지는
# 무조건 한 번씩 다 지나가야 한다.
# 즉, 좌표의 최댓값과 최솟값 사이의 거리를 구하라
n = int(input())

matrix = list(map(int,input().split()))

print(max(matrix) - min(matrix))