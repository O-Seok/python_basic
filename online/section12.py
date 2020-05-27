# Section12-1
# 파이썬 데이터베이스 연동 (SQLite)
# 테이블 생성 및 삽입

import sqlite3
import datetime

# 삽입 날짜 생성
now = datetime.datetime.now()
print('now: ', now)

nowDatetime = now.strftime('%Y-%m-%d %H:%M:%S')
print('nowDatetime: ', nowDatetime)

# sqlite3
print('sqlite3.verseion: ', sqlite3.version)
print('sqlite3.sqlite_version: ', sqlite3.sqlite_version)


# DB 생성 & Auto Commit(Rollback)

# sqlite3.connect() 로 생성
# Commit을 해줘야 최종적으로 DB적용 실행
# isolation_level = None 으로 Auto Commit 을 설정해준다.
conn = sqlite3.connect('/Users/claudjung/Documents/dev/python_basic/resource/database.db', isolation_level = None)

# Cursor 
# 데이터, 파일의 제일 끝부분을 가져온다.
# 그렇기 때문에 cursor를 가져오면 제일 데이터의 끝부분 부터 시작한다.
c = conn.cursor()
print('Cursor Type: ',type(c))

# 테이블 생성 (Data Type : TEXT, NUMERIC, INTEGER, REAL, BLOB )
c.execute("CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY, \
  username text, email text, phone text, website text, residate text)")

# 데이터 삽입
c.execute("INSERT INTO users VALUES(1, 'Jeong', 'totkfa789@gmail.com', '010-0000-0000', 'Jeong.com', ? )", (nowDatetime,))

# 데이터 삽입 2
c.execute("INSERT INTO users(id, username, email, phone, website, residate) VALUES (?, ?, ?, ?, ?, ?)", (2, 'Park', 'Park@gmail.com', '010-1111-1111', 'Park.com', nowDatetime,))

# Many 삽입(튜플, 리스트)
userList = (
  (3, 'Lee', 'leenave.com', '010-2222-2222', 'Lee.com', nowDatetime),
  (4, 'Cho', 'Cho@.com', '010-3333-3333', 'Cho.com', nowDatetime),
  (5, 'Yoo', 'You@.com', '010-4444-4444', 'You.com', nowDatetime)
)

c.executemany("INSERT INTO users(id, username, email, phone, website, residate) VALUES (?, ?, ?, ?, ?, ?)", userList)


# 테이블 데이터 삭제
# conn.execute("DELETE FROM users")

# print("users db deleted : ", conn.execute("DELETE FROM users").rowcount)

# commit: isolation_level: None 일 경우 자동 반영 (auto commit)
# conn.commit()

# 롤 백
# conn.rollback()

# 접속 해제
conn.close()