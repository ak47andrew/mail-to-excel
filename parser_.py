from typing import Any, Optional, Type
from stream import StringStream
import datatype as dt
from config import str_to_entry, str_to_type
from converters import convert


def parser(stream: StringStream) -> list[dt.Entries]:
    output = []
    entry_data: dict[str, Any] = {}
    entry_type: Optional[Type[dt.Entries]] = None

    while True:
        value = next(stream)
        if value is None:
            break
        value = value.replace("\t", " ")
        print(value)

        if value == "-----------------------" and entry_data:
            assert entry_type is not None
            output.append(
                entry_type(**entry_data)
            )
            entry_data.clear()
            continue

        if ":" in value:
            part1, *part2 = value.split(":")
            part1 = part1.strip().lower().replace(" ", "")
            part2 = ":".join(part2).strip()

            # check for entery
            entery = str_to_entry.get(part1)
            if entery is not None:
                entry_type = entery
                continue

            # check for data
            data = str_to_type.get(part1)
            if data is not None:
                key, datatype = data
                entry_data[key] = convert(part2, datatype)
                continue

    return output
 