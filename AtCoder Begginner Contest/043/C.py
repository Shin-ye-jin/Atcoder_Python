# C - Be Together
n = int(input())
matrix = list(map(int,input().split()))
s=0

num = round(sum(matrix)/len(matrix),0)
# 리스트의 합계 sum 사용
# round 함수 사용하여 반올림 하기

for i in matrix:
    s = s + pow(i-num,2) # pow 사용하여 거듭제곱 하기

print(int(s)) # float형으로 되어 있기 때문에 int로 변환

# !! round 함수를 생각!