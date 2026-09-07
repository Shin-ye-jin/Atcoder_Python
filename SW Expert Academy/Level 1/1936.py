# 1936 1대1 가위바위보
a,b = map(int,input().split())

if b+1>3:
    if a == (b+1)-3:
        print("A")
else:
    if a == (b+1):
        print("A")

if a+1>3:
    if b == (a+1)-3:
        print("B")
else:
    if b == (a+1):
        print("B")

# n1,n2 = map(int,input().split())
#
# dict = {1:3, 2:1, 3:2}
#
# def rock_sissor_paper(n1,n2):
#     if dict[n1] == n2:
#         return "A"
#     else:
#         return "B"