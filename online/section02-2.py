# Section02-2
# python 기초 코딩
# 몸풀기 코딩 실습

# import this
import sys 

# python 기본 인코딩
# python3 부터는 기본 인코딩이 입력/출력은 utf-8 이다.
print(sys.stdin.encoding)
print(sys.stdout.encoding)

# 출력문
print('my name is Goodboy!')

# 변수 선언
myName = 'Goodboy'

# 조건문 
if myName == 'Goodboy':
    print('OK')

# 반복문
for i in range(1, 10):
    for j in range(1, 10):
        print('%d * %d = ' % (i, j), i*j)

# 변수 선언(한글)로도 가능, 하지만 권고되지는 않음!! 자유도가 그만큼 높다!!
이름 = '좋은사람'

# 출력
print(이름)

# 함수선언
def hello():
    print('안녕하세요. 반갑습니다.')

hello()

# 클래스
class Cookis:
    pass

# 객체 생성 ( 클래스 생성, 객체 생성)
cookis = Cookis()

print(id(cookis))
print(dir(cookis))