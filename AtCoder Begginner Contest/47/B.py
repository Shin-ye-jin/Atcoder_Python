# B Sunke's Coloring 2(ABC Edit)

# x < xi 영역을 칠함 => 왼쪽 경제(x_min)를 오른쪽으로 이동
# x > xi 영역을 칠함 => 오른쪽 경계(x_max)를 왼쪽으로 이동
# y < yi 영역을 칠함 => 아래쪽 경계(y_min)를 위로 이동
# y > yi 영역을 칠함 => 위쪽 경계(y_max)를 아래로 이동
import sys

def solve():
    try:
        line = sys.stdin.readline().split()
        if not line: return
        W, H, N = map(int, line)
    except ValueError:
        return

    x_min, x_max = 0, W
    y_min, y_max = 0, H

    for _ in range(N):
        x, y, a = map(int, sys.stdin.readline().split())

        if a == 1:
            x_min = max(x_min, x)
        elif a == 2:
            x_max = min(x_max, x)
        elif a == 3:
            y_min = max(y_min, y)
        elif a == 4:
            y_max = min(y_max, y)

    width = max(0, x_max - x_min)
    height = max(0, y_max - y_min)

    print(width * height)

if __name__ == "__main__":
    solve()

# x_min = 0, x_max = W / x에서 가장 작은 값인 x_min
# y_min = 0, y_max = H / y에서 가장 작은 값인 y_min
# a가 1이라면 오른쪽으로 이동해야 해서 x_min의 값이 더 큰 값인 xi로 업데이트
# a가 2라면 왼쪽으로 가야함 즉 더 작은 xi의 값을 x_max의 값으로 초기화함
# a가 3이라면 위로 가야하기 때문에 y_min의 값을 yi의 값으로 초기화
# a가 4라면 아래로 가야하기 때문에 y_max의 값을 yi의 값으로 초기화 함
