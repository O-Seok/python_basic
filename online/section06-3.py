# Section06-3
# 람다식
# : 메모리 절약, 가독성 향삭, 코드 간결
#   함수는 객체 생성 -> 리소스(메모리) 할당
#   람다는 즉시 실행(heap 초기화) -> 메모리 초기화

# 일반적 함수 -> 변수 할당
def mul_10(num: int) -> int:
  return num * 10

var_func = mul_10
print(var_func)
print(type(var_func))

print(var_func(10))

# 람다식 변환
# x 인자를 의미한다.
print()
print('<< lamda식 변환 >>')
lamda_mul_10 = lambda x: x * 10

print('>>>', lamda_mul_10(10))

# 함수에 만들어진 함수, 람다식을 인자로도 줄 수 있고, 받을 수도 있다.
print()
print('함수에 만들어진 함수, 람다식을 인자로도 줄 수 있고, 받을 수도 있다')
def func_final(x, y, func):
  print( x * y * func(10))

func_final(10, 10, lamda_mul_10)

# 즉시 lambda 식을 만들어서 넘겨줄 수도 있다.
print()
print('즉시 lambda 식을 만들어서 넘겨줄 수도 있다.')
print(func_final(10, 10, lambda x : x * 1000))

