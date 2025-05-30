# B - Unhappy Hacking (ABC Edit)
matrix = list(input())
res = []

for i in range(len(matrix)):
    if matrix[i] == '0':
        res.append('0')
    elif matrix[i] == '1':
        res.append('1')
    elif matrix[i] == 'B':
        if len(res) > 0:
            res.pop()

print("".join(res))

# join 활용법!!