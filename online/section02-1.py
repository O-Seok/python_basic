# Section02-1
# 파이썬 기초 코딩
# print 구문의 이해
# print 함수는 출력 함수이다 !

# 기본출력
print('Hello Python!')
print("Hello Python!")
print("""Hello Python!""")
print('''Hello Python!''')

print()

# Separator 옵션 사용
print('T', 'E', 'S', 'T', sep='')
print('2019', '02', '19', sep='-')
print('niceman', 'google.com', sep='@')

# End 옵션 사용
print('welcome to', end=' ')
print('the black parade', end=' ')
print('piano notes')
print('testtest')
print()

# format 사용 [] , {}, ()
print('{} and {}'.format('You', 'me'))
print('{0} and {1}, and {0}'.format('You', 'me'))
print('{a} are {b}'.format(a='you', b='me'))

# %s : 문자, %d = 정수, %f = 실수
print("%s's favorite number is %d" %('Cluad', 3))

print("Test1: %5d, price: %4.2f" %(776, 6534.123))
print("Test1: {0: 5d}, pricce: {1: 4.2f}".format(776, 6534.123))
print("Test1: {a: 5d}, pricce: {b: 4.2f}".format(a=776, b=6534.123))

"""
참고 : Escape 코드

\n : 개행
\t : 탭
\\ : 문자
\' : 문자
\" : 문자
\r : 캐리지 리턴
\f : 폼 피드
\a : 벨 소리
\b : 백 스페이스
\000 : 널 문자
'''
"""

print("'you'")
print('\'you\'')
print('"you"')
print("""'you'""")
print('\\you\\')
print('\\you\\\n\n\n')
print('test')
print('\t\t\ttest')