# B - A to Z String
matrix = list(input())

a,b=0,0
for i in range(len(matrix)):
    if matrix[i] == 'A':
        a = i
        break

for i in range(len(matrix)):
    if matrix[i] == 'Z':
        b = i

print(b-a+1)