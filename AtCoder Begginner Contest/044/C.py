# C - Tak and Cards !! 공부
# n,a = map(int,input().split())
# matrix = list(map(int,input().split()))
# res1 = []
# res2 = []
# for i in range(n-1):
#     for j in range(i+1,n):
#         print("1")
#         res1.append(matrix[i]+matrix[j])
#         print(matrix[i]+matrix[j])
#
#     for j in range(len(res1)):
#         res1.append(matrix[i]+res1[j])
#         print(matrix[i]+res1[j])
#
# print(res1)

# 다시...

# import numpy as np
#
# n,a = list(map(int,input().split()))
# cards = list(map(int,input().split()))[:n]
#
# maxnumber = n*a
#
# dp = np.zeros((n+1,n+1,n*a+1),dtype=int)
#
# dp[0][0][0] = 1
#
# for i in range(n):
#     for j in range(i+1):
#         for k in range(maxnumber):
#             if dp[i][j][k] >0:
#                 # print('k',k)
#                 dp[i+1][j][k] += dp[i][j][k]
#
#                 if k+cards[i] <= maxnumber:
#                     #print('i',i,'j',j,'k',k)
#                     # print(k+cards[i])
#                     dp[i+1][j+1][k+cards[i]] += dp[i][j][k]
#                     #print(dp[i+1][j+1][k+cards[i]])
#
# result = 0
#
# for j in range(1,n+1):
#     result += dp[n][j][a*j]
#     print(dp[n][j][a*j])
#
# print(result)

n,a=map(int,input().split())
L=list(map(int,input().split()))
dp=[[0]*(50*50+1) for _ in range(n+1)]
dp[0][0]=1

for e in L:
    for i in range(n)[::-1]:
        for j in range(2500):
            if dp[i][j]:
                print(e)
                dp[i+1][j+e]+=dp[i][j]
ans=0

for i in range(1,n+1):
  ans+=dp[i][a*i]
print(ans)

# 0(1개) -> 8
# 1(2개) -> 7+9 / 7+9
# 2(3개) -> 7+9+8 / 7+8+9

# e가 7일 때 7로 1개
# e가 9일 때 9 / 16 로 2개
# e가 8일 때 8 / 15 17 / 24 4개
# e가 9일 때 9 / 16 18 17 / 25 24 26 / 33 8개

# -> 0일 때 8, 1일 때 16 2개, 2일 때 24 2개 5개
