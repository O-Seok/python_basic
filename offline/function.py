# 함수 선언
def do_nothing():
  # 선언만 하고 아무것도 하지 않음
  pass

def do_sum(a, b):
  return a + b

# type hinting 적용
def do_sum(a: int, b: int) -> int:
  return a + b

def is_odd_number(number: int) => bool:
  return number % 2

# 위치 인자
def send_email(sender, receiver, title, body):
  pass

# 키워드 인자
def send_email(sender, reciever, title='new Email', body='New Email'):
  print(sender, reciever, title, body)

#