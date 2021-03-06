# Section11
# 파이썬 외부 파일 처리
# 파이썬 Excel, csv 파일 읽기 및 쓰기

# CSV : MIME - text/csv

import csv

# 예제 1
with open('./resource/sample1.csv', 'r', encoding='CP949') as f:
  reader = csv.reader(f)

  # 확인
  # print(reader)
  # print(type(reader))
  # print(dir(reader))
  # print()

  for c in reader:
    print(c)

# # 예제 2
with open('./resource/sample2.csv', 'r', encoding='CP949') as f:
  reader = csv.reader(f, delimiter='|')


  # 확인
  # print(reader)
  # print(type(reader))
  # print(dir(reader))
  # print()

  for c in reader:
    print(c)


# 예제 3 ( Dict변환 )
with open('./resource/sample1.csv', 'r', encoding='CP949') as f:
  reader = csv.DictReader(f)

  for c in reader:
    for k, v in c.items():
      print(k, v)
    print('---------------')
    

# 예제 4 
w = [[1,2,3], [4,5,6], [7,8,9], [10,11,12], [13,14,15], [16,17,18]]

with open('./resource/sample3.csv', 'w') as f:
  wt = csv.writer(f)

  for v in w:
    wt.writerow(v)


# 예제 5
with open('./resource/sample4.csv', 'w') as f:
  wt = csv.writer(f)
  wt.writerows(w)

# XSL, XLSX
# openpyxl, xlsxwriter, xlrd, xlwt, xlutils
# pandas를 주로 이용(openpyxl, xlrd)

# pip install xlrd
# pip install openpyxl
# pip install pandas


# excel 파일 열어보기
import pandas as pd

# sheetname='시트명' 또는 숫자, header= 숫자, skiprow= 숫자
xlsx = pd.read_excel('./resource/sample.xlsx')

# 상위 데이터 확인
# head(): 처음부터 5개까지
print(xlsx.head())

# 데이터 확인
# tail(): 끝에서 5개까지
print(xlsx.tail())

# 데이터 확인
# 행, 열
print(xlsx.shape) 

# 엑셀 or CSV 다시 쓰기
xlsx.to_excel('./resource/result.xlsx', index=False)
xlsx.to_csv('./resource/result.csv', index=False)


