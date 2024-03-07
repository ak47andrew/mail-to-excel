from dataclasses import dataclass as dc
from datetime import datetime


class Entries:
    def format(self): pass


@dc
class MaternityLeave(Entries):
    worker: str
    date: tuple[datetime, datetime]
    post: str
    code: int
    unit: str

    def format(self):
        return [
            self.worker, 
            self.post, 
            f"с {self.date[0].strftime('%d.%m.%Y')} по {self.date[0].strftime('%d.%m.%Y')}", 
            self.unit
        ]

@dc
class Transfer(Entries):
    worker: str
    date: datetime
    post: str
    working_rate: float
    unit: str
    order: str

    def format(self):
        return [
            self.worker,
            self.post,
            self.date.strftime('%d.%m.%Y'),
            self.unit
        ]

@dc
class Reception(Entries):
    worker: str
    date: datetime
    post: str
    unit: str
    order: str
    employee_code: str

    def format(self):
        return [
            self.worker,
            self.post,
            self.date.strftime('%d.%m.%Y'),
            self.unit
        ]

@dc
class Layoffs(Entries):
    worker: str
    date: datetime
    post: str
    code: int
    unit: str
    grounds_for_dismissal: str
    order: str

    def format(self):
        if "(" in self.worker:
            return [
                self.worker.split(" (")[0],
                self.post,
                self.date.strftime('%d.%m.%Y'),
                self.unit,
                self.worker.split(" (")[1][:-1],
            ]
        return [
            self.worker,
            self.post,
            self.date.strftime('%d.%m.%Y'),
            self.unit,
            "",
        ]
