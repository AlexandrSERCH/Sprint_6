from dataclasses import dataclass
from enum import Enum
from faker import Faker

fake = Faker('ru_RU')

class MetroStation(Enum):
    SOKOLNIKI = "Сокольники"
    UNIVERSITY = "Университет"

class DeliveryDate(Enum):
    TOMORROW = "завтра"
    DAY_AFTER_TOMORROW = "послезавтра"

class RentalPeriod(Enum):
    ONE_DAY = "сутки"
    WEEK = "семеро суток"

class Color(Enum):
    BLACK = "чёрный жемчуг"
    GREY = "серая безысходность"


@dataclass
class TestData:
    first_name: str
    last_name: str
    address_delivery: str
    metro_station: MetroStation
    phone: int
    delivery_date: DeliveryDate
    rental_period: RentalPeriod
    color: Color
    comment: str


def get_order_datasets():
    return [
        TestData(
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            address_delivery=f"{fake.street_name()} {fake.random_int(1, 5000)}",
            metro_station=MetroStation.SOKOLNIKI,
            phone=fake.random_int(70000000000, 79999999999),
            delivery_date=DeliveryDate.TOMORROW,
            rental_period=RentalPeriod.ONE_DAY,
            color=Color.BLACK,
            comment=fake.text()
        ),
        TestData(
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            address_delivery=f"{fake.street_name()}{fake.random_int(1, 5000)}",
            metro_station=MetroStation.UNIVERSITY,
            phone=fake.random_int(70000000000, 79999999999),
            delivery_date=DeliveryDate.DAY_AFTER_TOMORROW,
            rental_period=RentalPeriod.WEEK,
            color=Color.GREY,
            comment=fake.text()
        )
    ]


