n = int(input())

for i in range(n):
    sum = 0
    number = list(map(int,input().split()))

    for x in number:
        sum += x
    print(f"#{i+1} {sum/10:.0f}")