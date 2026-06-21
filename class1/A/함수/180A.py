# 상자에 공이 N개 있을 때, A개를 빼고 B개를 더하는 수량 변화 함수

def count_balls(n, a, b):
    return n - a + b

N, A, B = map(int, input().split())
# 100 2 1 순서대로 입력
print(count_balls(N, A, B))