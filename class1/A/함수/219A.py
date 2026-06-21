# 현재 점수 X를 받아 다음 등급 커트라인(40점)까지 몇 점이 남았는지 계산하라

def next_level_score(score):
    if score < 40:
        print(40 - score)
    elif score < 70:
        print(70 - score)
    elif score < 90:
        print(90 - score)
    else:
        print("expert")

X = int(input()) # 90 입력
next_level_score(X)