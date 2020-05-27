# 클래스
class Car:
  def __init__(self, name, color):
    self.name = name
    self.color = color

  def call_car_name(self):
    print('Car name is : ', self.name)
  
  def call_car_color(self):
    print('Car color is : ', self.color)


first = Car('bmw', 'blue')
print(first.name)
first.name = 'sonata'
print(first.name)
print(first.color)
first.call_car_name()
first.call_car_color()

print("'-----------------------------------------'")

second = Car('benz', 'red')
print(second.name)
print(second.color)
second.call_car_name()
second.call_car_color()

print("'-----------------------------------------'")

# 클래스 상속
class Person:
  def __init__(self, name, age, tall):
    self.name = name
    self.age = age
    self.tall = tall

  def print_name(self):
    print('Your name is : ', self.name)
  
class Phone_number(Person):
  def __init__(self, name, age, tall, phone):
    super().__init__(name, age, tall)
    self.phone = phone

  def print_super_name(self):
    print('Your super name is : ', self.name)
  
  def print_both_super_child(self):
    super().print_name()
    print('print_both_super_child')

  # override
  def print_name(self):
    print('override super method!!')

a = Phone_number('Jeong', 29, 180, '010-0000-0000')

print(a.name)
print(a.age)
print(a.tall)
print(a.phone)
a.print_name()
a.print_super_name()
a.print_name()

print("'-----------------------------------------'")

# get/set
# @Property

class Person:
  def __init__(self, name):
    self.hidden_name = name

  @property
  def name(self):
    return self.hidden_name

  @name.setter
  def name(self, name):
    self.hidden_name = name

p = Person('Park')
print(p.name)
p.name = 'Lee'
print(p.name)


print("'-----------------------------------------'")

# 클래스 메소드
# self, cls
# @classmethod

class Person:
  count = 0
  def __init__(self):
    Person.count += 1

  def added_count_instance(self):
    Person.count += 1

  @classmethod
  def added_count_class(cls):
    cls.count += 1
  
  @classmethod
  def call(cls):
    print('Class method all: ', cls.count)


a = Person()
b = Person()
c = Person()

Person.call()
a.added_count_instance()
Person.call()

Person.added_count_class()
Person.call()















