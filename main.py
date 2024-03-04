from stream import StringStream
from parser_ import parser
from formatter_ import format
from os import listdir

all_entries = []

for file in listdir():
    if not file.endswith(".txt"):
        continue

    with open(file, encoding="windows-1251") as f:
        lines = f.read().splitlines()

    stream = StringStream(lines)

    data = parser(stream)

    all_entries.extend(data)

format(all_entries)
