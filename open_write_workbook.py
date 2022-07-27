from itertools import product
import openpyxl
dog = ['labrador', 'german', 'pug']
age = [1, 5, 10]
country = ['India', 'Germany', 'Italy']

wb=openpyxl.Workbook()
ws=wb.active
ws.title="permutation"
for p in product(dog,age,country):
    ws.append(p)
wb.save(filename="permutation.xlsx")
