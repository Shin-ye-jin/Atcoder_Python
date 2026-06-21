# 사과 1개를 사는 금액 X원, 사과 3개를 한 묶음으로 사는 금액 Y원, 정확히 얼마를 지불해야 N개를 사과를 살 수 있는가?

X, Y, N = map(int,input().split())
# X는 10, Y는 40, N은 10
if X*3 > Y:
    n = N//3
    m = N%3
    print(n*Y + m*X)
else:
    print(X*N)
