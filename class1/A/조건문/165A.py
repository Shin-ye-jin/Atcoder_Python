# a,b 사이의 숫자 중 k의 배수가 있다면 OK, 없다면 NG를 출력하라.

k = int(input()) # 7 입력
a, b = map(int, input().split())
# 500 600 입력

res = b // k * k
if res >= a and res <= b:
   print("OK")
else:
   print("NG")
