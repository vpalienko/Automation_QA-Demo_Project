from dataclasses import dataclass


@dataclass
class Person:
    full_name: str = None
    first_name: str = None
    last_name: str = None
    age: int = None
    email: str = None
    salary: int = None
    department: str = None
    current_address: str = None
    permanent_address: str = None
    mobile: str = None


@dataclass
class Date:
    date: str = None


@dataclass
class DateAndTime(Date):
    time: str = None