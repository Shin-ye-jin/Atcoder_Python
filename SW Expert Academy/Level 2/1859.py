# 1859 백만 장자 프로젝트

# 제일 뒤에 있는 숫자를 가장 비싼 매도가로 지정
# 역순으로 하나씩 비교하면서 오늘 매매가가 가장 비싼 매도가보다 작다면 시세차익이 생김
# 오늘 매매가가 더 크다면 가장 비싼 매도가가 해당 매매가로 변경됨.
import sys

n = int(sys.stdin.readline().strip())

for i in range(n):
    m = int(sys.stdin.readline().strip())
    matrix = list(map(int, sys.stdin.readline().split()))
    max_price = matrix[-1]
    total = 0
    for j in range(m-1,-1,-1):
        if max_price > matrix[j]:
            total = total + max_price-matrix[j]
        elif max_price < matrix[j]:
            max_price = matrix[j]
    print(f"#{i+1} {total}")