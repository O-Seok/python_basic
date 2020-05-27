# 문자 2번 문제
def count_substring(string, sub_string):
    li = ""
    c = 0
    for v in range(0, len(string)):
        li += string[v]
        print(li)
        if li.count(sub_string):
            c += 1
            li = li[li.find(sub_string)+1:]
    return c

po = 'ABCDCDC'
pb = 'CDC'
count_substring(po, pb)

# 문자 4번 문제
# def wrap(string, max_width):
#     pa = string
#     result = ""
#     a = pa[0:max_width]
#     result += a + "\n"
#     pa = pa[max_width:]
#     b = pa[0:max_width]
#     result += b + "\n"
#     pa = pa[max_width:]
#     c = pa[0:max_width]
#     result += c + "\n"
#     pa = pa[max_width:]
#     d = pa[0:max_width]
#     result += d + "\n"
#     pa = pa[max_width:]
#     e = pa[0:max_width]
#     result += e + "\n"
#     pa = pa[max_width:]
#     f = pa[0:max_width]
#     result += f + "\n"
#     pa = pa[max_width:]
#     g = pa
#     result += g
#   return result

# os = 'ABCDEFGHIJKLIMNOQRSTUVWXYZ'
# on = 4

# wrap(os, on)
# 문자 문제 5번
def print_formatted(number):
  print(number)
  # your code goes here
  # 기본 문자열 길이에 해당하는 nulspace 정의
  
  # 17번 돌려서 각 수마다 출력 하게 만들자.
  for i in range(1, number+1):
    # 1~17 의 10진수, 8진수, 16진수, 2진수 값을 알아낸다.
    num = i
    octNum = format(i, 'o')
    hexNum = format(i, 'X')
    byNum = format(i, 'b')
    
    nullSize = len(format(number, 'b'))

    # 각각의 해당하는 널 공간 계산
    numNull = ''.rjust(nullSize-len(str(num)))
    octNumNull = ''.rjust(nullSize-len(str(octNum)))
    hexNumNull = ''.rjust(nullSize-len(str(hexNum)))
    byNumNull = ''.rjust(nullSize-len(str(byNum)))

    print("{0}{1} {2}{3} {4}{5} {6}{7}".format(numNull, num, octNumNull, octNum, hexNumNull, hexNum, byNumNull, byNum))
  return 'ok'

print_formatted(17)


# ---------------------------------------------------------------------------- #
# 리스트 2번 문제
# if __name__ == '__main__':
#     n = int(input())
#     li = []
#     for i in range(0, n):
#         con = input()
#         vali = con.split(" ")
#         if vali[0] == 'insert':
#             x, y, z = vali
#             li.insert(int(y), int(z))
#         elif vali[0] == 'remove':
#             x, y= vali
#             li.remove(int(y))
#         elif vali[0] == 'append':
#             x, y = vali
#             li.append(int(y))
#         elif vali[0] == 'pop':
#             li.pop()
#         elif vali[0] == 'reverse':
#             li.reverse()
#         elif vali[0] == 'sort':
#             li.sort()
#         elif vali[0] == 'print':
#             print(li)


# 리스트 3번 문제
# if __name__ == '__main__':
#     students = []
#     points = []
#     for _ in range(int(input())):
#         name = input()
#         score = float(input())
#         students.append([name, score])
#         points.append(score)

#     points.sort()
#     point = points[1]
    
#     result = []
#     for i in range(len(students)):
#         if students[i][1] == point:
#             showperson = ""
#             showperson += students[i][0]
            
#             result.append(showperson)
#     result.sort()
#     for v in result:
#         print(v)

# ------------------------------------------------------------ #
# if __name__ == '__main__':
#     students = []
#     point = 0
#     person = []
#     for _ in range(int(input())):
#         name = input()
#         score = float(input())
#         students.append([name, score])
        
#     students = sorted(students, key= lambda student : student[1])
#     point = students[1][1]
    
#     for i in range(len(students)):
#         if students[i][1] == point:
#             person.append(students[i][0])
#     person.sort()
#     for v in person:
#         print(v)

