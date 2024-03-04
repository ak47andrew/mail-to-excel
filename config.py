from datetime import datetime
from typing import Type
import datatype as dt


str_to_type: dict[str, tuple[str, type]] = {
    "работник": ("worker", str),
    "времяотпуска": ("date", tuple[datetime, datetime]),
    "должность": ("post", str),
    "шифр": ("code", int),
    "подразделение": ("unit", str),

    "датаперевода": ("date", datetime),
    "ставка": ("working_rate", float),
    "приказ": ("order", str),

    "датаприема": ("date", datetime),
    "кодсотрудника": ("employee_code", str),

    "датаувольнения": ("date", datetime),
    "основаниеувольнения": ("grounds_for_dismissal", str)
}

str_to_entry: dict[str, Type[dt.Entries]] = {
    "отпускпоуходузаребенком": dt.MaternityLeave,
    "переведены": dt.Transfer,
    "приняты": dt.Reception,
    "уволены": dt.Layoffs,
}

entry_to_name = {
    dt.MaternityLeave: ("Декрет", ["ФИО", "Должность", "Срок", "Подразделение"]),
    dt.Transfer: ("Перевод", ["ФИО", "Новая должность", "Дата", "Новое подразделение"]),
    dt.Reception: ("Прием", ["ФИО", "Должность", "Дата приема", "Подразделение"]),
    dt.Layoffs: ("Увольнения", ["ФИО", "Совместительство", "Должность", "Дата увольнения", "Подразделение"]),
}

entry_list = [dt.Layoffs, dt.MaternityLeave, dt.Transfer, dt.Reception]
