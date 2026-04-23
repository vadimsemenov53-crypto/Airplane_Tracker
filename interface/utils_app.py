import time

from src.api_client import APIAircraft, APICoordinates
from src.country_repository import CountryRepository
from src.flight_repository import FlightRepository
from typing import Any


def ask_user() -> str:
    """Вспомогательная функция для взаимодействия с пользователем."""
    return input("Пользователь: ")


def show_message(message: str) -> None:
    """Вспомогательная функция вывода в консоль сообщения от программы."""
    print(f"\nПрограмма:\n{message}")


def writing_api_to_tables(country_repo: CountryRepository, flights_repo: FlightRepository) -> None:
    """ Вспомогательная функция осуществляющая запросы к API и добавляющая данные в таблицу. """
    list_country = ["France", "Germany", "Italy", "Spain", "Sweden", "Poland", "Greece", "Portugal", "Netherlands",
                    "Austria"]

    api_geo = APICoordinates()
    api_air = APIAircraft()

    for country in list_country:
        api_geo.get_response_api(country)
        api_geo.get_coordinates()
        data_country = api_geo.data_response

        api_air.get_response_api(api_geo.coordinates)
        data_air = api_air.aeroplanes

        country_repo.insert_info(data_country)
        flights_repo.insert_info(data_air)

        time.sleep(2)  # для избежания ограничения по запросам.


def iterator(data: list[dict[str, Any]]) -> None:
    """ Вспомогательная функция для вывода информации в консоль. """
    for i in data:
        print(i)
