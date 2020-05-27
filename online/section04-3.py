# section04-3
# python data type
# List
# 순서 O, 중복 O, 수정 O, 삭제 O
# 배열, 모음, 


# List 선언
a = []
b = list()
c = [1, 2, 3, 4]
d = [10, 100, 'Pen', 'Bana', 'Orange']
e = [10, 100, ['Pen', 'Bana', 'Orange']]

print(a)
print(b)
print(c)
print(d)
print(e)


# 인덱싱
print(d[3], d[-2])
print(d[0] + d[1])
print(e[2][1])
print(e[-1][-2])

# 슬라이싱
print(d[0:3])
print(d[0:1])
print(d[0:2])
print(e[2][1:3])

# 연산
print(c + d)
print(c * 3, len(c * 3))
print(str(c[0]) + 'hi')

# list 수정
c[0] = 77
print(c)

# 슬라이싱 처리하여 값을 할당하면, list 안에 값으로 할당이 된다.
c[1:2] = [100, 1000, 10000]
print(c)

# 슬라이싱 처리하여 값을 할당하는 것과 다르게, 인덱스를 지정하여 값을 할당해주면 list 형태로 중첩, 할당된다.
c[1] = ['a', 'b', 'c']
print(c)

# list 삭제
del c[1]
print(c)

del c[-1]
print(c)


print()
print()
print()


# list 함수
y = [5, 2, 3, 1, 4]
print(y)

# append = 끝에 추가
y.append(6)
print(y)

# sort = 순서대로 줄세우기
y.sort()
print(y)

# reverse = 역순으로 줄세우기
y.reverse()
print(y)

# insert = 원하는 인덱스에 값을 수정
y.insert(2, 7)
print(y)

# remove = 인덱스를 지우는게 아니라, 원하는 데이터 값을 지정하여 삭제할 수 있다.
y.remove(2)
print(y)

# pop = 맨 마지막 값을 꺼내고, 나머지를 출력한다.
y.pop()
print(y)

# extend = 끝에 값으로 할당 / 반면에 append로 하면 긑에 list 형태로 들어가진다.
ex = [88, 77]
# y.extend(ex)
y.append(ex)
print(y)

y.extend(ex)
print(y)


# list 컴프리헨션(Comprehension)
print()
print('list 컴프리헨션')

# 일반적인 list 만들기
numbers = []
for n in range(1, 100):
  numbers.append(n)

print(numbers)

print()

# 컴프리헨션 이용하여 list 만들기
numbers2 = [x for x in range(1, 101)]
print(numbers2)

print()
# list 컴프리헨션 안에 if 문도 가능하다.
p5 = ['갑', '을', '병', '정']
rep5 = [v for v in p5 if v != '정']
print(rep5)

print()
# 튜플 ( 순서 0 , 중복 0, 수정 x, 삭제 x)
a = ()
b = (1,)
c = (1, 2, 3, 4)
d = (10, 100, ('a', 'b','c'))

print(a)
print(b)
print(c)
print(d)

# 튜플 인덱싱
print(c[2])
print(c[3])
print(d[2][1])

# 튜플 슬라이싱
print(d[2:])
print(d[2][0:2])

# 튜플 연산
print(c + d)
print(c * 3)
print()


# 튜플 함수
z = (5, 2, 1, 3, 4, 1)
print(z)
print(3 in z)
print(z.index(5))
print(z.count(1))