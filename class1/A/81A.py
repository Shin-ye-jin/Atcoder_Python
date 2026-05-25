# 101처럼 세 자리 문자열이 주어짐. 1은 구슬이 있는 칸, 0은 비어있는 칸, 구슬이 총 몇개?

S = input()
ans = 0

for character in S:
    if character == '1':
       ans += 1

print(ans)