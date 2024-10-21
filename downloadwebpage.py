import xlrd
from statistics import mean, median

wb = xlrd.open_workbook('salaries.xlsx') #открываем файл
sheet_index = wb.sheet_by_index(0)#выбираем активный лист
sh = wb.sheet_names()#название этого листа
ls = dict()
vals = [sheet_index.row_values(rownum) for rownum in range(sheet_index.nrows)]   # получаем значения из всех ячеек



for i in vals[1:]:
    ls[i[0]] = sum([_ for _ in i[1:]]) / 8
print(vals)
print(ls)
print(sorted(ls.items(), key= lambda x: x[1], reverse=True)[0][0])



