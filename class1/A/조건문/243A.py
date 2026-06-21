# 샴푸가 V만큼 남아있다. 아빠가 A만큼 썼을 때 남은 양이 0보다 작아지면 F를 출력, 남으면 M을 출력

V, A, B, C = map(int,input().split())
if V - A < 0:
    print("F")
else:
    print("M")
