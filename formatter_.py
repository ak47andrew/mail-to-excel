import datatype as dt
from config import entry_list, entry_to_name
from openpyxl import Workbook


def format(enteries: list[dt.Entries]):
    wb = Workbook()

    ws = wb.active

    for entry_type in entry_list:
        title, format = entry_to_name[entry_type]

        ws.append([])
        ws.append([title])
        ws.append(format)

        for entry in filter(lambda x: isinstance(x, entry_type), enteries):
            ws.append(entry.format())

    wb.save("sample.xlsx")
