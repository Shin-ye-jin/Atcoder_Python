# 1204 [S/W 문제 해결 기본] 1일차 - 최빈수 구하기

n = int(input())

for i in range(n):
    m = int(input())
    matrix = list(map(int, input().split()))
    result = [0 for _ in range(101)]
    for number in matrix:
        result[number] += 1

    max_count = 0 # 가장 높은 빈도수
    mode_score = 0 # 최빈값 점수

    for i in range(101):
        if result[i] >= max_count:
            max_count = result[i]
            mode_score = i

    print(f"#{m} {mode_score}")