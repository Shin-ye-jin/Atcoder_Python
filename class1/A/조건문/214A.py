# 3일 동안의 날씨 정보가 문자열로 주어짐. 비가 오면 R, 맑으면 S임. 비가 연속으로 최대 며칠 동안 왔는지 출력 (RRS는 2일 RSR은 1일)

S = input()
if S == "RRR":
   print(3)
elif "RR" in S:
   print(2)
elif "R" in S:
   print(1)
else:
   print(0)