# Section10
# 파이썬 예외처리의 이해

# 예외 종류
# 문법적으로 에러가 없지만, 코드 실행(런타임) 프로세스에서 발생하는 예외 처리도 중요하다.
# linter : 코드 스타일, 문법 체크


# syntaxError : 잘못된 문법
# print('Test)
# if True
#   pass
# x => y

# NameError : 참조변수가 없을 때
# a = 10
# b = 15
# print(c)

# ZeroDivisionError : 0 나누기 에러
# print(10 / 0)

# IndexError : 인덱스 범위 오버
# x = [10, 20, 30]
# print(x[3])

# keyError 
# dic = {'name': 'Kim', 'Age': 33, 'City': 'Seoul'}
# print(dic['hobby'])

# AttributeError : 모듈, 클래스에 있는 잘못된 속성 사용시에 예외
# import time
# print(time.month())

# ValueError : 참조 값이 없을 때 발생
# x = [1, 5, 9]
# x.remove(10)
# x.imdex(10)

# FileNotFoundError : 외부 파일 처리할 때 주로 발생
# f = open('text.txt','r')

# typeError
# x = [1, 2]
# y = (1, 2)
# z = 'test'
# print(x + y)


# ------------------------------------------------------ #
# 항상 예외가 발생하지 않을 것으로 가정하고 먼저 코딩
# 그 후 런타임 예외 발생 시, 예외 처리 코딩 권장(EAFP 코딩 스타일)
# ------------------------------------------------------ #


# 예외 처리 기본
# try : 에러가 발생할 가능성이 있는 코드 실행
# except : 에러명1
# except : 에러명2
# else : 에러가 발생하지 않았을 경우 실행
# finally : 항상 실행

name = ['Kim', 'Lee', 'Park']

# 예제 1
# 어떤 에러가 발생할 지 안다면, except (에러종류): 로 작성한다.
try:
  z = 'Kim'
  # z = 'Cho'
  x = name.index(z)
  print('{} Found it! in name'.format(z, x+1))
except ValueError:
  print('Not found it ! - Occurred ValueError')
else:
  print('OK! else')


# 예제 2
# 어떤 에러가 발생할 지 모를 떄는 except: 만으로 작성한다.
try:
  # z = 'Kim'
  z = 'Cho'
  x = name.index(z)
  print('{} Found it! in name'.format(z, x+1))
except :
  print('Not found it ! - Occurred Error')
else:
  print('OK! else')

# 예제 3
# finally 는 에러가 발생하든 발생하지 않든 간에 실행된다.
# else는 에러가 발생하지 않은 경우 실행된다.
try:
  # z = 'Kim'
  z = 'Cho'
  x = name.index(z)
  print('{} Found it! in name'.format(z, x+1))
except :
  print('Not found it ! - Occurred Error')
else:
  print('OK! else')
finally:
  print('finally OK!')


# 예제 4
# 예외 처리는 하지 않지만, 무조건 수행되는 코딩 패턴

try:
  print('Try')
finally:
  print('OK Finally!!!!!')



# 예제 5
# 계층적으로 에러는 잡을 수도 있다.
# except Exception:은 모든 에러를 잡는 것이기 때문에 맨 마지막 순서로 작성한다.
try:
  z = 'Kim'
  # z = 'Cho'
  x = name.index(z)
  print('{} Found it! in name'.format(z, x+1))
except ValueError:
  print('Not found it ! - Occurred Error')
except IndexError:
  print('Not found it ! - Occurred Error')
except Exception:
  print('Not found it ! - Occurred Error')
else:
  print('OK! else')
finally:
  print('finally OK!')


# 예제 6
# 예외 발생 : raise
# raise 키워드로 예외 직접 발생

try:
  a = '333'
  if a == 'Kim':
    print('ok 허가!')
  else:
    raise ValueError
except ValueError:
  print('문제 발생 !')
except Exception as f:
  print(f)
else:
  print('OK !')


