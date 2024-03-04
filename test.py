from openpyxl import Workbook
wb = Workbook()

ws = wb.active

ws.append([])
ws.append(["Увольнения"])
ws.append(["ФИО", "Должность", "Дата увольнения", "Подразделение"])

wb.save("sample.xlsx")
