# 양배추 N개를 사려고 한다. A번째 양배추까지는 1개당 X원, 그 이후부터는 1개당 Y원이다. N개가 A개보다 작거나 같을 때 총 가격을 구해라.

N, A, X, Y = map(int,input().split())
# N 5, A 3, X 20, Y 15
res = A*X + (N-A)*Y
print(res)
