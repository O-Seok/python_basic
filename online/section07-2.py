# Section07-2
# 파이썬 클래스 상세 이해
# 상속, 다중상속

# 예제 1
# 상속 기본
# 슈퍼클래스(부모) 및 서브클래스(상속 된 자식) -> 모든 속성, 메소드 사용 가능

# 라면 -> 속성(종류, 회사, 맛, 면 종류, 이름) : 부모

class Car:
  """Parent Class"""
  def __init__(self, tp, color):
    self.type = tp
    self.color = color

  def show(self):
    return 'Car Class "Show Method!"'


class BmwCar(Car):
  """Sub Class"""
  def __init__(self, car_name, tp, color):
    super().__init__(tp, color)
    self.car_name = car_name

  def show_model(self) -> None:
    return "Your Car Name: %s" %self.car_name


class BenzCar(Car):
  """Sub Class"""
  def __init__(self, car_name, tp, color):
    super().__init__(tp, color)
    self.car_name = car_name

  def show_model(self) -> None:
    return "Your Car Name: %s" %self.car_name

  def show(self):
    print(super().show())
    return 'Car Info : %s %s %s' %(self.car_name, self.type, self.color)



# 일반 사용
model1 = BmwCar('520d', 'sedan', 'red')

print(model1.color)     # super
print(model1.type)      # super
print(model1.car_name)  # sub
print(model1.show())    # super
print(model1.show_model()) # sub
print(model1.__dict__)

print()
# method Overriding ( 오버라이딩 )
# 부모에게 상속 받은 메소드를 필요에 따라 다시 재정의 한 것을 오버라이딩이라 한다.
model2 = BenzCar('220d', 'sedan', 'blue')
print(model2.show())


print()
# Parent Method Call
model3 = BenzCar('350s', 'sedan', 'silver')
print(model3.show())


# Inheritance Info (상속정보)
# mro()
print(BmwCar.mro())
print(BenzCar.mro())


print()
# 예제 2
# 다중 상속


class X:
  pass

class Y:
  pass

class Z:
  pass

class A(X, Y):
  pass

class B(Y, Z):
  pass

class M(B, A, Z):
  pass

print(M.mro())
print(A.mro())


# print()
# testCar = Car()
# testCar.testShow()