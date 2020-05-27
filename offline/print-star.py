star = "*"
null_str = " "

print("1. --------------------------- ", end="\n\n")
# star 찍기 1번 문제
m = 5
for i in range(m, 0, -1):
  print(star * i)


print()
print("2. --------------------------- ", end="\n\n")
# star 찍기 2번 문제
n = 5
for i in range(0, n):
  if i != 0:
    print(" " * i, end='')
  for j in range(n-i, 0, -1):
    print("*", end='')
  print()


print()
print("3. --------------------------- ", end="\n\n")
# star 찍기 3번 문제
l = 7
for i in range(1, l+1):
  for j in range(l-i):
    print(" ", end='')
  for k in range((2 * i) - 1):
    print("*", end='')
  print()


