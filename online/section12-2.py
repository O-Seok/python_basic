# Section12-2
# 파이썬 데이터베이스 연동 (SQLite)
# 테이블 조회

import sqlite3

# DB파일 조회(없으면 새로 생성)
conn = sqlite3.connect('/Users/claudjung/Documents/dev/python_basic/resource/database.db')

# 커서 바인딩
c = conn.cursor()

# 데이터 조회(전체)
c.execute("SELECT * FROM users")

# 커서 위치가 변경
# 1개 로우 선택
# print('One -> \n', c.fetchone())

# 지정 로우 선택
# print('Three -> \n', c.fetchmany(size = 3))

# # 전체 로우 선택
# print('all -> \n', c.fetchall())

# 모든 데이터를 다 가져온 상태 이므로, 커서는 맨 끝부분에 위치, 커서는 현재 위치의 상태를 기억한다.
# none이 나온다.
# print('all -> \n', c.fetchall())

print()

# 순회 1
# rows = c.fetchall()
# for row in rows:
#   print('retrieve1 >', row)

# 순회 2
# for row in c.fetchall():
#   print('retrieve2 >', row)

# 순회 3
# for row in c.execute("SELECT * FROM users ORDER BY id desc"):
#   print('retriev 3 >', row)


print()

# WHERE Retrieve1
# param1 = (3,)
# c.execute("SELECT * FROM users WHERE id = ?", param1)
# print('param1', c.fetchone())

# # WHERE Retrieve2
# param2 = 4
# c.execute('SELECT * FROM users WHERE id = "%s"' % param2)
# print('param2', c.fetchone())

# # WHERE Retrieve3
# c.execute('SELECT * FROM users WHERE id = :Id' , {"Id": 5})
# print('param3', c.fetchone())

# # WHERE Retrieve4
# param4 = (3, 5)
# c.execute("SELECT * FROM users WHERE id IN(?,?)", param4)
# print('param4', c.fetchall())

# # WHERE Retrieve5
# c.execute("SELECT * FROM users WHERE id IN('%d','%d')" % (3, 4))
# print('param5', c.fetchall())

# # WHERE Retrieve6
# c.execute("SELECT * FROM users WHERE id=:id1 OR id=:id2", {"id1": 2, "id2": 5})
# print('param6', c.fetchall())

print()


# # Dump 출력
with conn:
  with open('/Users/claudjung/Documents/dev/python_basic/resource/dump.sql','w') as f:
    for line in conn.iterdump():
      f.write('%s\n' % line)

    print('Dump Print Complete')


# f.close(), conn.close()