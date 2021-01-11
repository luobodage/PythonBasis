import xlrd
from xlutils.copy import copy
import time

start = time.time()
data = xlrd.open_workbook('housing.xls')
sheet = data.sheet_by_index(0)
nrow = sheet.nrows
ncols = sheet.ncols
print(nrow, ncols)
for i in range(nrow):
    if sheet.cell(i,0) == -121.39:
        print(sheet.cell(i,0))

end = time.time()

print(end - start)