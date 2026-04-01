# B - Choose Integers
# A의 배수들을 몇 개든(중복 가능) 골라서 다 더햇을 때
# 그 합을 B로 나눈 나머지가 C가 될 수 있는가?"
# 5로 나누었다면 나머지는 0,1,2,3,4 가 나오면 이것이 반복됨
# 즉 2로 나누었으면 나머지는 2개뿐! 이런 것

a,b,c = map(int,input().split())
n = 0

for i in range(1,b+1):
    if a*i % b == c:
        n=1

if n==1:
    print("YES")
else:
    print("NO")