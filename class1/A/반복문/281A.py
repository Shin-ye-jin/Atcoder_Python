# 정수 N이 주어진다. N부터 시작해서 0까지 숫자를 한 줄에 하나씩 거꾸로 다운 카운트하며 출력

N = int(input()) # 3 입력

for i in range(N, -1, -1):
    print(i)