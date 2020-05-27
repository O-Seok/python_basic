# Section07-1 

# class
# 파이썬 클래스 상세 이해하기
# self, 클래스, 인스턴스 변수

# 클래스, 인스턴스 차이 중요
# 네임스페이스 : 객체를 인스턴스화 할 때 저장된 공간
# 클래스 변수 : 직접 사용 가능, 객체 보다 먼저 생성
# 인스턴스 변수 : 객체마다 별도로 존재

# 기본적인 선언 
# class는 첫글자는 대문자!
# 그냥 선언만 해놓으면 클래스 안에 pass를 넣어두어 에러가 안나도록 한다.

# def __init__() : 기본적으로 클래스에서 구현해놔야 하는 메소드(함수), 
#                 클래스를 최초 초기화 할 때 구현해주어야 한다.


# class (클래스명): 
#  (클래스에 관련한 함수들)

class ClassInfo:
  # 속성 : 이름, 나이, 전화번호, 회사이름, 색깔 등등 `정보`
  # 메소드 : 걷는다, 쓴다, 입는다, 누르다, 말한다 등등 `행동`

  # def __init__(): 클래스 초기화, 제일 기본적으로 작동
  def __init__(self):
    print("초기화")

# 인스턴스 한다: 변수에 클래스를 할당하는 것을 말한다.
ex = ClassInfo()

# 예제 1

class UserInfo:

  def __init__(self, name, height, weight):
    self.name = name
    self.height = height
    self.weight = weight
  def user_info_p(self):
    print('name: ', self.name)
    print('height: ', self.height)
    print('weight: ', self.weight)

# 유저 1의 정보
user1 = UserInfo("Kim", 190, 80)
user1.user_info_p()

print(user1.name)
print(user1.height)
print(user1.weight)


# 유저 2의 정보
user2 = UserInfo("park", 170, 50)
user2.user_info_p()

print(user2.name)
print(user2.height)
print(user2.weight)


# id()는 메모리 저장 값을 알 수 있다.
print(id(user1))
print(id(user2))

# 네임스페이스 : 인스턴스가 가지고 있는 자기 자신의 저장공간
print(user1.__dict__)
print(user2.__dict__)


# 클래스를 생성하고, 인스턴스 한다.
# 인스턴스 변수들의 네임스페이스는 독립적이다.


# 예제 2
# self의 이해
# self를 인자로 받는 메소드(함수)는 인스턴스화 되었을 때 사용할 수 있는 인스턴스 함수이다.
# 클래스 안의 함수 중 인자를 self로 받지 않는 함수는 클래스 함수
# 클래스 안의 함수 중 인자를 self로 받는 함수는 인스턴스 함수

class SelfTest:
  def function1():
    print('function1 called!')
  def function2(self):
    print('function2 called!')

SelfTest.function1()

test = SelfTest()
test.function2()

# 예제 3
# 클래스 변수: 공유 O
# 인스턴스 변수: 공유 X
# 인스턴스 네임 스페이스에 값이 없으면, 클래스 네임 스페이스에서 찾아서 값을 찾아온다.

class WareHouse:
  # 클래스 변수
  stock_num = 0
  def __init__(self, name):
    self.name = name
    WareHouse.stock_num += 1
  def __del__(self):
    WareHouse.stock_num -= 1

user1 = WareHouse('Kim')
user2 = WareHouse('Pard')
user3 = WareHouse('Lee')

print(user1.__dict__)
print(user2.__dict__)
print(user3.__dict__)
print(WareHouse.__dict__)

print(user1.name)
print(user2.name)
print(user3.name)

print(user1.stock_num)
print(user2.stock_num)
print(user3.stock_num)

# 인스턴스 삭제
# del (인스턴스 변수)

