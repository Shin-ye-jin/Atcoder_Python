# N개의 숫자가 리스트로 주어진다. 이 리스트에 들어있는 모든 숫자의 합을 구해라.

N = int(input()) # 입력 3
nums = list(map(int,input().split()))
# 입력 2 7 2
# 리스트의 모든 원소를 싹 다 더해주는 sum() 함수

print(sum(nums))