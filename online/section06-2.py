# Section06-2
# 함수

# 중첩함수(클로저)
# 함수 안에 함수
# 참고 : 데코레이터오 클로저(http://schoolofweb.net/blog/posts/%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EB%8D%B0%EC%BD%94%EB%A0%88%EC%9D%B4%ED%84%B0-decorator/)
print('<< 중첩함수 >>')
print('예제 1')
def nested_func(num):
  def function_in_func(num):
    print('>>>', num)
  print('in function')
  function_in_func(num + 1000)

nested_func(10000)

# 힌트 : 인자를 어떤 타입을 받는지, 출력 값은 어떠한 데이터 타입인지 설명해줄 수 있다.
# 예제 6 
print()
print('<< 힌트 >>')
def func_mul3(x : int) -> list:
  y1 = x * 100
  y2 = x * 200
  y3 = x * 300
  return [y1, y2, y3]

print(func_mul3(5))