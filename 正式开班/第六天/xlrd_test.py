import xlrd
from xlutils.copy import copy

path = 'test.xls'
book = xlrd.open_workbook(path)
sheet = book.sheet_by_index(0)
# print(sheet.cell(1,2))
for i in range(sheet.nrows):
    for j in range(sheet.ncols):
        print(sheet.cell(i, j).value, end=' ')
    print()
nrows = sheet.nrows
book_copy = copy(book)
sheet_copy = book_copy.get_sheet(0)
data = [201,202,203,204,205,206]
for i in range(len(data)):
    sheet_copy.write(nrows,i,data[i])
book_copy.save("test.xlsx")
