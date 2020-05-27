# 10.1 파일

# os

# 파일 존재 확인: exists()

# . : 현재 위치
# .. : 부모 위치


# ---------------------------------------------------------------------------- #

# JSON

# 요청 / 응답  - 통신
# string만 가능

# 시리얼라이즈 : 데이터의 어떤 형태()라던지간에 그 형태로 생긴 string값으로 변환하여 보내는 것을 말한다.

# dumps() : 결과물은 다른 서버/클라이언트 간 주고 받을 수 있는 눈에 보이는 문자열
# json.dumps(data)

# 디시리얼라이즈: string화 되어 있는 data를 우리가 아는 데이터 타입으로 바꿔준다.
# loads() : 결과물은 stirng화 되어 있는 데이터를 원래의 데이터 타입으로 바꿔준다.
# json.loads(data)

# django 프레임워크는 요청이 왔을 시 디시리얼라이즈, 응답 해줄 떈 시리얼라이즈를  내부적으로 알아서 해준다.



# --------------------------------------------------------------------------- #
# 달력과 시간
# 날짜와 시간은 포맷이 매우 다양
# date, time, datetime


# date
from datetime import date

fool_day = date(2020, 4, 1)
print(fool_day)

print(fool_day.year, fool_day.month, fool_day.day, fool_day.weekday())

print('-----------------------------------------------------')
# timedelta
from datetime import date
from datetime import timedelta

today = date.today()
one_day = timedelta(days=1)

yesterday = today - one_day
print('today : "%s", yesterday : "%s"' % (today, yesterday))

print('-----------------------------------------------------')
# time
from datetime import time

t = time( 15, 30, 45)
print(t.hour, t.minute, t.second, t.microsecond)

print('-----------------------------------------------------')
# datetime
from datetime import datetime, date, time

now = datetime.now()
print(now)
print(now.year, now.month, now.day, now.hour, now.minute, now.second, now.microsecond)

# combine
today = date.today()
night = time(18)
tonight = datetime.combine(today, night)
print(today, night, tonight, sep='\n')