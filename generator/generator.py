from data.data import Person, Date, DateAndTime
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
        permanent_address=faker_en.address().replace("\n", ", "),
        mobile=faker_en.msisdn()[:10]
    )


def generated_subjects():
    subjects_list = ["Hindi", "English", "Maths", "Physics", "Chemistry", "Biology", "Computer Science", "Commerce",
                     "Accounting", "Economics", "Arts", "Social Studies", "History", "Civics"]
    number_of_subjects = random.randint(1, len(subjects_list))
    random_subjects = random.sample(subjects_list, number_of_subjects)
    return random_subjects


def generated_state_and_city():
    states_and_cities = {"NCR": ["Delhi", "Gurgaon", "Noida"], "Uttar Pradesh": ["Agra", "Lucknow", "Merrut"],
                         "Haryana": ["Karnal", "Panipat"], "Rajasthan": ["Jaipur", "Jaiselmer"]}
    random_state = random.choice(list(states_and_cities.keys()))
    random_city = random.choice(states_and_cities[random_state])
    return random_state, random_city


def generated_colors():
    colors = ["Red", "Blue", "Green", "Yellow", "Purple", "Black", "White", "Voilet", "Indigo", "Magenta", "Aqua"]
    return colors


def generated_date():
    return Date(
        date=faker_en.date(pattern="%B %#d %Y")
    )


def generated_time():
    hours = random.randint(0, 23)
    minutes = random.randrange(0, 46, 15)
    return f"{hours:02d}:{minutes:02d}"


def generated_date_and_time():
    return DateAndTime(
        date=faker_en.date(pattern="%B %#d %Y"),
        time=generated_time()
    )