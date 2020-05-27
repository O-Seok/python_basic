# Section09
# 파일 읽기, 쓰기

# 읽기 모드 : r, 쓰기 모드(기존 파일 삭제): w, 추가 모드(파일 생성 또는 추가): a
# .. : 상대경로, . : 절대 경로

# 기타 : https://docs.python.org/3.7/library/functions.html#open

# 파일 읽기
# 예제 1

# 파일을 열 때는 open()
f = open('./resource/review.txt', 'r')
content = f.read()

print(content)
print(dir(f))
# 반드시 close 리소스 반환
f.close()

print('-----------------------------------')
print('-----------------------------------')

# 예제 2
# with 는 마지막에 close를 안 해줘도 된다.
with open('./resource/review.txt','r') as f:
  c = f.read()
  print(c)
  print(list(c))
  print(iter(c))

print('-----------------------------------')
print('-----------------------------------')

# 예제 3
with open('./resource/review.txt','r') as f:
  for c in f:
    print(c.strip())


print('-----------------------------------')
print('-----------------------------------')

# 예제 4
with open('./resource/review.txt','r') as f:
  for c in f:
    content = f.read()
    print(">", content)
    content = f.read() # 여기서부턴 내용이 없다.
    print(">", content)


print('-----------------------------------')
print('-----------------------------------')


# 예제 5
with open('./resource/review.txt','r') as f:
  line = f.readline()
  # print(line)
  while line :
    print(line, end='')
    line = f.readline()

print('-----------------------------------')
print('-----------------------------------')

# 예제 6
with open('./resource/review.txt','r') as f:
  contents = f.readlines()
  print(contents)
  for c in contents:
    print(c, end=' ******')


print('-----------------------------------')
print('-----------------------------------')

# 예제 7
score = []
with open('./resource/score.txt','r') as f:
  
  for line in f:
    score.append(int(line))
  print(score)

print('Average : {:6.3}'.format(sum(score)/len(score)))

print('-----------------------------------')
print('-----------------------------------')

# 파일 쓰기

# 예제 1
with open('./resource/test.txt','w') as f:
  f.write('Niceman!\n')

# 예제 2
with open('./resource/test.txt','a') as f:
  f.write('Goodman!\n')

# 예제 3
from random import randint

with open('./resource/test2.txt','w') as f:
  for cnt in range(6):
    f.write(str(randint(1, 50)))
    f.write('\n')

# 예제 4
# writelines: 리스트 -> 파일로 저장
with open('./resource/test3.txt','w') as f:
  li = ['Kim\n', 'Park\n', 'Cho\n']
  f.writelines(li)

# 예제 5
로그가 파일안에 찍힌다.
with open('./resource/test4.txt','w') as f:
  print('Test Contest1!', file=f)
  print('Test Contest1!', file=f)