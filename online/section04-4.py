# section04-4
# 파이썬 데이터 타입 (자료형)
# 딕셔너리, 집합 자료형

# 딕셔너리(Dictionary) : 순서 x, 중복 x, 수정 o, 삭제 o ( key는 중복 X, value는 중복 O)
# key, value (Json) -> MongoDB

# 딕셔너리 선언
a = {'name': 'Jeong', 'phone': '010-9999-9999', 'birth': '890928'}
b = {0: 'Hello Python', 1: 'Hello Coding'}
c = {'arr':[1, 2, 3, 4, 5]}

print(type(a))
print(a)
print(b)
print(c)



# 출력
print(a['name'])
print(a.get('name'))
print(a.get('address'))
print(c.get('arr'))
print(c.get('arr')[1:3])


# 딕셔너리 추가
a['address'] = 'Seoul'
print(a)
a['rank'] = [1, 2, 3]
a['rank2'] = (1, 2, 3,)
print(a)


# 딕셔너리도 이러한 함수들로 출력을 할 수 있을까?
print(2 in b)
print(2 not in b)
print('name' in a)


print()
# keys, values, items
# keys(), values() 등 함수로 호출 하면 각각의 값들이 리스트 형태처럼 출력이 되지만, 이때 인덱싱을 하면 에러가 발생한다.
# 이때 해결법은 list() 형변환 함수를 통해서 list로 형변환 후, 인덱싱 처리가 가능하다.
print(a.keys())           
print(list(a.keys()))

temp = list(a.keys())
print(temp[1:3])

print(a.values())
print(list(a.values()))

# items() 함수는 리스트 형식 안에 key와 value를 한 쌍으로 하는 튜플 형식으로 출력이 된다. 하지만 이 때도 값으로 어떠한 처리를
# 하기 위해서는 list() 형변환 함수를 이용하여 list로 형변환 후, 원하는 처리를 하면 된다. 
print()
print(a.items())
print(list(a.items()))

tems =  list(a.items())
print(tems[0])
print(tems[0][0])
print(tems[0][0][:2])

print()
print()



# 집합 (set) : 순서 x, 중복 x, 수정 o, 삭제 O
# 집합 선언
a = set()
b = set([1, 2, 3, 4])
c = set([1, 4, 5, 6, 6])

print(type(a))
print(c)

# set은 주로 튜플이나 리스트로 변환해서 처리한다.
t = tuple(b)
print(t)
l = list(b)
print(l)

print()
print()

s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])

# 교집합
print(s1.intersection(s2))
print(s1 & s2)

# 합집합
print(s1 | s2)
print(s1.union(s2))

# 차집합
print(s1 - s2)
print(s1.difference(s2))

# set 추가 & 제거 가능
s3 = set([7, 8, 9, 10, 15])
s3.add(18)

print(s3)

s3.remove(15)
print(s3)

print(type(s3))
