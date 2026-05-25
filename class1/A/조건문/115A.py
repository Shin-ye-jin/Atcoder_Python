# 입력으로 날짜 D가 주어짐. 25일이면 Christmas, 24일이면 Christmas Eve, 23일이면 Christmas Eve Eve, 22일이면 Christmas Eve Eve Eve를 출력

D = int(input())
if D == 25:
   print("Chirstmas")
elif D == 24:
   print("Christmas Eve")
elif D == 23:
   print("Christmas Eve Eve")
else:
   print("Christmas Eve Eve Eve")