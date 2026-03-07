# B - Template Matching
# 1. 시작점 (0,0)에서 비교 : A의 (0,0)~(1,1) 영역과 B를 비교
# A의 부분 : #. / .#
# B의 모양 : .# / #.
# 불일치
# 2. 시작점 (0,1)에서의 비교 : A의(0,1) ~ (1,2) 영역과 B를 비교
# A의 부분 : .# / #.
# B의 모양 : .# / #.
# 일치

# 완전 탐색으로 풀 수 있다. 모든 가능한 시작 위치를 다 조사함

import sys

def solve():
    # N(큰 그림 크기), M(작은 그림 크기) 입력
    n, m = map(int ,sys.stdin.readline().split())

    a = [sys.stdin.readline().strip() for _ in range(n)]
    b = [sys.stdin.readline().strip() for _ in range(m)]

    # 시작점 (i,j)를 순회 (N-M 까지만 가야함)
    for i in range(n-m+1):
        for j in range(n-m+1):

            is_match = True
            for r in range(m): # 시작지점에서 B와 일치하는지 체크
                for c in range(m):
                    if a[i+r][j+c] != b[r][c]:
                        is_match = False
                        break
                if not is_match:
                    break

            if is_match: # 일치하는 지점을 찾았다면 종료한다.
                print("Yes")
                return

    print("No") # 끝까지 못 찾았다면 No

solve()