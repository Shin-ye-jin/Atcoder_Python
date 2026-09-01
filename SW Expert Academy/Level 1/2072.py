n = int(input())

for i in range(n):
    numbers = list(map(int, input().split()))
    total = 0

    for x in numbers:
        if x % 2 == 1:
            total += x
    print(f"#{i + 1} {total}")