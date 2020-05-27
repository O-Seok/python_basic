# Section05-1 
# python 흐름제어(제어문)
# 조건문 실습

# boolean
print(type(True), type(False))
print('boolean')
# example 1
if True:
  print('Yes')

# example 2
if False:
  print('No')

# example 3
if False:
  print('No')
else:
  print('Yes')
  

# 관계연산자
# >, >=, <, <=, ==, !=
print()
print('관계연산자')
a = 10
b = 0

print(a == b)
print(a != b)
print(a > b)
print( a >= b)
print(a < b)
print( a<= b)


# 참 거짓 종류(True, False)
# 참 : "내용", [내용], (내용), {내용}, 1, True
# 거짓 : "", [], (), {}, 0, False
print()
print('참 거짓 종류별 출력')
city = ""
if city:
  print("True")
else:
  print("False")


# 논리 연산자
# and or not
print()
print('논리연산자')
a = 100
b = 60
c = 15

print('and : ', a > b and b > 3)
print('or : ', a > b or c > b)
print('not : ', not a > b)
print(not False)
print(not True)


# 산술, 관계, 논리 연산자
# 우선순위 : 산술 > 관계 > 논리  순서로 적용
print()
print('산술,관계,논리 연산자 순서')

print('ex1 : ', 5 + 10 > 0 and not 7 + 3 == 10)

score1 = 90
score2 = 'A'

if score1 >= 90 and score2 == 'A':
  print('합격 하셨습니다.')
else:
  print('죄송합니다. 불합격입니다.')

# 다중조건문
# if 다음의 또 다른 조건들이 필요하다면 elif를 통해서 여러가지 조건문을 주어서 흐름문을 이용할 수 있다.
print()
print('다중 조건문')

num = 70

if num >= 90:
  print('num 등급 A', num)
elif num >= 80:
  print('num 등급 B', num)
elif num >= 70:
  print('num 등급 C', num)
else:
  print('꽝')


# 중첩 조건문
print()
print('충접조건문')

age = 27
height = 175

if age >= 20:
  if height >= 170:
    print('A지망 지원 가능')
  elif height >= 160:
    print('B지망 지원 가능')
  else:
    print('지원 불가')
else:
  print('20세 이상 지원 가능')

