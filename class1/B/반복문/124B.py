# 바닷가에 n개의 건물이 왼쪽부터 차례대로 있고, 각 건물의 높이가 리스트로 주어진다. 맨 왼쪽부터 하나씩 건물을 보는데, 자기보다 왼쪽에 있는 건물보다 높거나 같으면 바다가 보인다. 해당 건물이 몇 개인지 출력하라.

n = int(input()) # 4 입력
h = list(map(int, input().split())) # 6 5 6 8 입력

count = 0
current_max = 0

for height in h:
    if height >= current_max:
      count += 1
      current_max = height

print(count)
