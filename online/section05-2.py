# Section05-2
# 파이썬 흐름제어(반복문)
# 반복문 실습

# 코딩의 핵심 -> 조건 해결 중요

# 기본 반복문: for, while

# while
print('while')

v1 = 1
while v1 < 11:
  print('v1 is : ', v1)
  v1 += 1


# for
print()
print('for')

# 0 ~ 9 까지 반복을 하고 싶다면,
for v2 in range(10):
  print('v2 is : ',v2)

# 1 ~ 9 까지 반복을 하고 싶다면,
for v3 in range(1, 10):
  print('v3 is : ', v3)

# 1부터 100까지의 합
print()
print('1부터 100까지의 합 구하기 ( for문 이용 )')
score = 0
for num in range(1, 101):
  score += num  

print(score)

# 1부터 100까지의 합 간단한 함수로 구하기! 
print('1 ~ 100 까지의 합 구하기(sum()함수 이용하기): ', sum(range(1, 101)))
print('1 ~ 100 까지의 짝수의 합을 구하라! ( sum()함수 이용 ): ', sum(range(1, 101, 2)))


# 시퀀스 ( 순서가 있는 ) 자료형 반복
# 문자열, 리스트, 튜플, 집합, 딕셔너리
# iterable 리턴 함수 : range, reversed, enumerate, filter, map, zip
print()
print('시퀀스(순서가 있는)')
names = ['Kim', 'Park', 'Cho', 'Yoo', 'Choi']

for v in names:
  print('You are : "', v)

word = "dreams"

for s in word:
  print('word : "', s)

my_info = {
  'name': 'Kim',
  'age': 33,
  'city': 'Seoul' 
}

# 딕셔너리 for문으로 원하는 값 출력하기
print()
print('딕셔너리에서 for문으로 원하는 값 출력하기')

# 기본 값은 키를 리턴한다.
for key in my_info:
  print('my_info', key)

# 값
for value in my_info.values():
  print('my_info_value', value)

# 키
for key in my_info.keys():
  print('my_info_key', value)

# 키 + 값
for item in my_info.items():
  print('my_info_item', item)  

print()



# 대문자일 때 , 소문자일 때 각각 반대로 출력
print('대문자는 소문자로, 소문자는 대문자로 출력하라.')
print('KennRY')

name = "KennRY"
for n in name:
  if n.isupper():
    print(n.lower())
  else:
    print(n.upper())


# for 문에서 사용하는 break
# break
# 내가 찾고자 하는 값이 반복문으로 돌아가는 중간에 있다면? 
# 내가 의도하는, 원하는 조건, 값이 나왔을 때 반복문에서 나올 때 사용한다.
print()
print('break문')

numbers = [14, 3, 4, 7, 10, 24, 17, 2, 33, 15, 34, 44, 38]

for num in numbers:
  if num == 33:
    print('found : 33 !')
    break
  else:
    print('not found : 33 !!')


# for - else 구문
# for 문 안에 break 구문이 작동이 되었다면, else 구문이 실행이 안되고, break문이 작동되지 않았다면 
# 마지막의 else 구문이 작동된다.
# 애초에 break가 없다면, for 문을 다 실행하고 마지막에 else가 실행이 된다.
print()
print('for - else 문')

numbers2 = [14, 3, 4, 7, 10, 24, 17, 2, 37, 15, 34, 44, 38]

for num in numbers2:
  if num == 33:
    print('found : 33 !')
    break
  else:
    print('not found : 33 !!')
else:
  print('not found 33 ..............')


# continue
# continue를 만나면 그 값은 넘어가고 다음 순서대로 간다. 조건문이 아닌 for문, 반복문으로 간다.
print()
print('continue')

lt = ['1', 2, 5, True, 4.3, complex(4)]

for v in lt:
  if type(v) is float:
    continue
  print('타입 : ', type(v))
else:
  print('End')