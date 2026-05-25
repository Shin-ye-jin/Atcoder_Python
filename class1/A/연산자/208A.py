# 6면짜리 주사위를 A번 던져서 눈의 합이 딱 B가 될 수 있는지 없는지 판별

A, B = map(int, input().split())

if A <= B <= 6*A:
   print("Yes")
else:
   print("No")