# section04-2 
# 문자열 생성 , 이스케이프 문자

str1 = "I am boy."
str2 = 'NiceMan'
str3 = ' '
str4 = str('')
print(len(str1), len(str2), len(str3), len(str4))

escape_str1 = "Do you have a \"big collection\""
print(escape_str1)
escape_str2 = "Tab\tTab\tTab"
print(escape_str2)



# Raw String
# 주로 경로같은 경우에 사용
raw_s1 = r'C:\Programs\Test\Bin'
print(raw_s1)
raw_s2 = r"\\a\\a"
print(raw_s2)



# 멀티라인
multi = """ 문자열 멀티라인 테스트 """
print(multi)

# 아래와 같이 줄이동하게 되는 경우 줄바꿈 문자열 선언 앞에 \ 를 붙여준다. python에서 \ 은 문자열이라고 인식하게 해준다.
multi2 = \
"""
문자열

멀티라인

테스트
"""
print(multi2)



# 문자열 연산
str_o1 = '*'
str_o2 = 'abc '
str_o3 = "def "
str_o4 = "Niecman"

print(str_o1 * 100)
print(str_o2 + str_o3)
print(str_o1 * 3)
print("a" in str_o4)
print("f" in str_o4)
print("f" not in str_o4)



# 문자열 형 변환
print(type(str(77)))
print(str(19.4) + 's')



# 문자열 함수
# 참고 : https://www.w3school.com/python/python_ref_string.asp

# a = 'niceman'
# b = 'orange'

# print(a.islower())
# print(a.isupper())
# print(b.endswith('e'))
# print(a.capitalize())
# print(a.replace('nice', 'Good'))
# print(list(reversed(b)))


# 문자열 슬라이싱
# 문자열은 인덱스가 정해지게 되어 바꿀 수가 없다. 이것을 '이뮤테이블' 이라한다.
# 이뮤테이블 = 수정 불가
# 뮤테이블 = 수정 가능
# 이뮤테이블 특성 때문에 원하는 부분을 슬라이싱 처리를 하여 원하는 값을 가진다.

a = 'niceman'
b = 'orange'

print(a[0:3])
print(a[0:4])
print(a[0:len(a)])
print(a[:4])
print(a[:])

print(b[0:4:2])   # 0부터 4전까지 출력하되, 2개씩 점프!
print(b[1:-2])
print(b[::-1])