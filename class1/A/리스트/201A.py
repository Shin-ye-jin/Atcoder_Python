# 알파벳 한 글자가 주어짐. 대문자면 A를 출력, 소문자면 a를 출력

def check_al(character):
    if character.isupper():
      return "A"
    else:
      return "a"

tmp = input()
print(check_al(tmp))