# Section05-3
# 파이썬 흐름제어(제어문)
# 제어문 관련 퀴즈(정답은 영상)

# 1 ~ 5 문제 if 구문 사용
# 1. 아래 딕셔너리에서 '가을'에 해당하는 과일을 출력하세요.
q1 =  {"봄": "딸기", "여름": "토마토", "가을": "사과"}
print('Q1 답은 : ')

for v in q1.items():
  if list(v)[0] == '가을':
    print(list(v)[1])
# 2. 아래 딕셔너리에서 '사과'가 포함되었는지 확인하세요.
q2 =  {"봄": "딸기", "여름": "토마토", "가을": "사과"}
print()
print('Q2 답은 : ')

for k, v in q2.items():
  if k == '사과':
    print('\'사과\'가 포함되어 있습니다.')
    print(k, v)
    break
else:
  print('사과없음')

# 3. 다음 점수 구간에 맞게 학점을 출력하세요.
# 81 ~ 100 : A학점
# 61 ~ 80 :  B학점
# 41 ~ 60 :  C학점
# 21 ~ 40 :  D학점
#  0 ~ 20 :  E학점
print()
print('Q3 답은:')

score = 61
if score > 80:
  print('A학점')
elif 60 < score <= 80:
  print('B학점')
elif 40 < score <= 60:
  print('C학점')
elif 20 < score <= 40:
  print('D학점')
else:
  print('E학점')

# 4. 다음 세 개의 숫자 중 가장 큰수를 출력하세요.(if문 사용) : 12, 6, 18
print()
print('Q4 답은:')

num1, num2, num3 = 12, 6, 18
# if num1 > num2 and num1 > num3:
#   print('제일 큰 수는: ', num1)
# elif num2 > num1 and num2 > num3:
#   print('제일 큰 수는: ', num2)
# else:
#   print('제일 큰 수는: ', num3)

print(max(num1, num2, num3))

# 5. 다음 주민등록 번호에서 7자리 숫자를 사용해서 남자, 여자를 판별하세요. (1,3 : 남자, 2,4 : 여자)
print()
print('Q5 답은:')

num = 134567
stnum = str(num)

if int(stnum[0]) == 1 or int(stnum[0]) == 3:
  print('남자')
elif int(stnum[0]) == 2 or int(stnum[0]) == 4:
  print('여자')
else:
  print('성별을 확인할 수 없습니다.')

# 6 ~ 10 반복문 사용(while 또는 for)

# 6. 다음 리스트 중에서 '정' 글자를 제외하고 출력하세요.
q3 = ["갑", "을", "병", "정"]
print()
print('Q6 답은:')

for v in q3:
  if v is "정":
    continue
  print(v)

# 7. 1부터 100까지 자연수 중 '홀수'만 한 라인으로 출력 하세요.
print()
print('Q7 답은:')

p = list(range(1, 101))
for v in p:
  if v % 2 != 0:
    print(v, end =',')

print()
# 8. 아래 리스트 항목 중에서 5글자 이상의 단어만 출력하세요.
q4 = ["nice", "study", "python", "anaconda", "!"]
print()
print('Q8 답은:')

for p in q4:
  if len(p) >= 5:
    print(p, end=' ')

print()
# 9. 아래 리스트 항목 중에서 소문자만 출력하세요.
q5 = ["A", "b", "c", "D", "e", "F", "G", "h"]
print()
print('Q9 답은:')

for sp in q5:
  if sp.islower():
    print(sp, end=' ')
  
print()
# 10. 아래 리스트 항목 중에서 소문자는 대문자로 대문자는 소문자로 출력하세요.
q6 = ["A", "b", "c", "D", "e", "F", "G", "h"]
print()
print('Q10 답은:')

print(q6)
for spell in q6:
  if spell.islower():
    print(spell.upper(), end=' ')
  else:
    print(spell.lower(), end=' ')
