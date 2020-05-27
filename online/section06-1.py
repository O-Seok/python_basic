# Section06-1
# Python 함수식 및 람다(lamda)

# 함수(function)
# 어떠한 반복적이고 중복되는 프로그래밍을 피할 수 있다.
# 하나의 기능을 하는 함수를 만들어야 좋다.
# 함수 선언 위치 중요

# 함수 정의 방법
# def 함수명(parameter):
#   code

# 함수 호출
# 함수명(), 함수(parameter)

# 함수 선언 위치 중요
# 함수를 사용할 위치보다 위에서 선언을 해주고, 선언한 위치보다 아래에서 사용한다.

# 예제 1
print()
print('함수 예제 1')
def hello(word):
  print('Hello ', word)

hello('Python!')
hello(7777)

# 예제 2 리턴이 있는 함수
print()
print('함수 예제2 리턴이 있는 함수')
def hello_return(word):
  val = "Hello " + str(word)
  return val

str = hello_return("python!!!!!!!")
print(str)

# 예제 3 다중리턴
print()
print('예제 3 다중리턴')

def func_mul(x):
  y1 = x * 100
  y2 = x * 200
  y3 = x * 300
  return y1, y2, y3

val1, val2, val3 = func_mul(100)
print(type(val1), val2, val3)

# 예제 4 다중리턴(데이터 타입변환)
print()
print('예제 4 다중리턴(데이터 타입변환)')

def func_mul2(x):
  y1 = x * 100
  y2 = x * 200
  y3 = x * 300
  return [y1, y2, y3]

lt = func_mul2(100)
print(lt, type(lt))

# 예제 4
# *args 매개변수가 몇개가 넘어갈지 모를때, 매개변수가 넘어오는거에 따라서 함수가 다르게 작동할 때
#       다양한 매개변수 형태를 받아서 함수의 흐름이 바뀌는 기능을 원할 때
#       결과 값이 튜플 형태로 나온다.

print()
print('예제 4 *args')

def args_func(*args):
  print(args)

args_func('kim')
args_func('kim','park')

print()
print('예제 5')

def args_func2(*args):
  for t in args:
    print(t)

args_func2('kim')
args_func2('kim','park')


# 이때 enumerate()함수를 사용하여, 인덱스와 값을 출력해줄 수도 있다.
print()
print('예제 6')

def args_func3(*args):
  for i, v in enumerate(args):
    print(i, v)

args_func3('kim')
args_func3('kim','park')


# kwargs
# 딕셔너리형태로 인자로 받을 수 있고, 출력을 딕셔너리형태로 반환한다.
print()
print('kwargs')

def kwargs_func(**kwargs):
  print(kwargs)

kwargs_func(name1='kim', name2='Park', name3='Lee')

# 예제 7
print()
print('예제 7')

def kwargs_func2(**kwargs):
  for k, v in kwargs.items():
    print(k, v)

kwargs_func2(name1='kim', name2='Park', name3='Lee')


# 전체 혼합
# example_mul()에서 arg1, arg2는 필수 인자
# *args, **kwargs는 가상 인자라 한다.
print()
print('전체 혼합')

def example_mul(arg1, arg2, *args, **kwargs):
  print(arg1, arg2, args, kwargs)

example_mul(10, 20)
example_mul(10, 20, 'park', 'kim', age1=24, age2=34)



