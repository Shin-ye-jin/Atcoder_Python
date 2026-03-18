# B - Picture Frame

h,w = map(int,input().split())

for i in range(w+2):
    print('#',end='')
print()
for i in range(h):
    n = input()
    print('#'+n+'#')

for i in range(w+2):
    print('#',end='')
