from datetime import datetime
from typing import Any


def convert(data: str, data_type: type):
    if data_type == str:
        return data
    elif data_type == int:
        return int(data)
    elif data_type == float:
        return float(data.replace(",", "."))
    elif data_type == datetime:
        return datetime.strptime(data, "%d.%m.%Y")
    elif data_type == tuple[datetime, datetime]:
        d = data.split()
        return datetime.strptime(d[1], "%d.%m.%Y"), datetime.strptime(d[3], "%d.%m.%Y")
    raise NotImplementedError(data_type)
