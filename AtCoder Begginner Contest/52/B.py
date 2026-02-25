# B - Increment Decrement
n = int(input())
m = list(input())

cnt = 0
res = list()

for i in range(n):
    if m[i] == "I":
       cnt+=1
    else:
        cnt-=1
    res.append(cnt)

if max(res)>=0:
    print(max(res))
else:
    print(0)