import os

ENV = os.getenv("ENV", "prod").lower()

URLS = {
    "prod": {
        "site": "https://qa-scooter.praktikum-services.ru/",
        "order": "https://qa-scooter.praktikum-services.ru/order",
    },
    "dev": {
        "site": "https://dev.qa-scooter.praktikum-services.ru/",
        "order": "https://dev.qa-scooter.praktikum-services.ru/order",
    },
}

def site_url():
    return URLS[ENV]["site"]

def order_url():
    return URLS[ENV]["site"]
