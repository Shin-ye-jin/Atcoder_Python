# 두 정수 X와 A가 주어짐. X가 A보다 작으면 0을 출력하고, X가 A보다 크거나 같으면 10을 출력하기

X, A = map(int, input().split())

if X < A:
     print(0)
else:
     print(10)