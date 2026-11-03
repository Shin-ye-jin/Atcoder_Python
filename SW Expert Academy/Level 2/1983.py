# 1983 조교의 성적 매기기

t = int(input())
avl = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']

for w in range(t):
  n, k = map(int, input().split())
  count = 0
  stu = {}
  res = []
  avl_tmp = []

  for i in range(10):
    for j in range(n // 10):
      avl_tmp.append(avl[i])

  for i in range(n):
    a, b, c = map(int, input().split())
    stu[i] = round(a * 0.35 + b * 0.45 + c * 0.2, 4)

  for number, score in stu.items():
    res.append(score)

  res.sort(reverse=True)

  for i in range(n):
    count += 1
    if stu[k - 1] == res[i]:
      print(f"#{w+1} {avl_tmp[count-1]}")
      break
# 기말고사 0.45인데 0.35라고 함 ㅋ!
# 1. 소수점 미세 오차를 방지하기 위해 round() 살짝 감싸주기
# 2. 부동소수점 안전 비교를 위해 소수점 자릿수 맞추기 혹은 값 비교
# 3. break로 사용하여 동점자 때문에 여러 번 찍히는 걸 막아준다

# 총점이 동일한 학생이 존재하지 않는다고 하여
# round와 break를 사용하지 않아도 될 것으로 보임
# 0.45를 사용하지 않아서 오류가 난것으로 파악

# t = int(input())
# avl = ['A+','A0','A-','B+','B0','B-','C+','C0','C-','D0']
#
# for w in range(t):
#     n, k = map(int, input().split())
#     count = 0
#     stu = {}
#     res = []
#     avl_tmp = []
#
#     for i in range(10):
#         for j in range(n//10):
#             avl_tmp.append(avl[i])
#
#     # print(avl_tmp)
#
#     for i in range(n):
#         a,b,c = map(int,input().split())
#         stu[i] = round(a*0.35+b*0.35+c*0.2,4)
#
#     for number, score in stu.items():
#         res.append(score)
#
#     # 역순 정렬
#     res.sort(reverse=True)
#
#     for i in range(n):
#         count+=1
#         if stu[k-1] == res[i]:
#             print(f"#{w+1} {avl_tmp[count-1]}")
#             break

# 1. 소수점 미세 오차를 방지하기 위해 round() 살짝 감싸주기
# 2. 부동소수점 안전 비교를 위해 소수점 자릿수 맞추기 혹은 값 비교

# print(res)
# print(stu)