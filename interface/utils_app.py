import time

from src.api_client import APIAircraft, APICoordinates

def ask_user() -> str:
    """Вспомогательная функция для взаимодействия с пользователем."""
    return input("Пользователь: ")


def show_message(message: str) -> None:
    """Вспомогательная функция вывода в консоль сообщения от программы."""
    print(f"\nПрограмма:\n{message}")


def api_request():
    """ Вспомогательная функция осуществляющая запросы к API. """
    list_country = ["France", "Germany", "Italy", "Spain", "Sweden", "Poland", "Greece", "Portugal", "Netherlands",
                    "Austria"]

    api_1 = APICoordinates()

    result_country = []
    result_airplanes = []

    for country in list_country:
        api_1.get_response_api("France",)
        result_country.append(api_1._data_response)

        api_1.get_coordinates()
        api_2 = APIAircraft()
        api_2.get_response_api(api_1.coordinates)
        data_air = api_2.aeroplanes

        time.sleep(2) # для избежания ограничения по запросам.
    print(result_country)

if __name__ == '__main__':
    api_request()
