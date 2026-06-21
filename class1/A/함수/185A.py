# 두 개의 숫자 중 더 작은 숫자를 찾아서 안전하게 리턴해주는 최솟값 판별 함수이다.

def find_min(a,b):
     return min(a, b)

a, b = map(int, input().split())
# 5 3 입력

print(find_min(a,b))
