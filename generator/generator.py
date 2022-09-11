from data.data import Person
from faker import Faker
import random

faker_en = Faker(locale="en_US")


def generated_person():
    return Person(
        full_name=faker_en.name(),
        first_name=faker_en.first_name(),
        last_name=faker_en.last_name(),
        age=random.randint(18, 65),
        email=faker_en.email(),
        salary=random.randint(1000, 15000),
        department=faker_en.job(max_length=25),
        current_address=faker_en.address().replace("\n", ", "),
        permanent_address=faker_en.address().replace("\n", ", ")
    )