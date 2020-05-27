person = {
  'name': 'Kim',
  'age': 23,
}

person.clear()
print(person)
person['email'] = 'kim@email.com'
print(person)
person['age'] = 14
print(person)

age = person.get('age')
print(age)
print(person.get('address'))

extra = {'age': 25}
person.update(extra)

print(person)


print()
from collections import namedtuple as nt

Point = nt('Point', ['x', 'y'])
p = Point(123, y=987)
print(p)

r = p[0] + p[1]
print(r)

x, y = p
print(x, y)


from collections import defaultdict

d = defaultdict()
d['a'] += 'hot'


print(d)


