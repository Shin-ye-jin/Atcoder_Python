# 바둑판 격자가 문자열 모양으로 주어진다. 각 줄마다 ‘#’ 모양이 총 몇 개 들어있는지 루프로 전부 세어서 합계를 출력

H, W = map(int, input().split())
total_sharp = 0
# 입력 #.... / ..... / .##..
for _ in range(H):
    row = input()
    total_sharp += row.count('#')

print(total_sharp)