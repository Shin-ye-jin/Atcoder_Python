# 두 정수 A,B를 입력받아 A+B, A-B, A/B 세 가지의 값 중 가장 큰 값을 출력해라

A, B = map(int, input().split())

results = [A+B, A-B, A/B]

print(max(results))