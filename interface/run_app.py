from interface.utils_app import show_message, ask_user
from src.api_client import APICoordinates, APIAircraft

def run_app():
    """ Основная функция для работы программы. """

    show_message("""Запуск PostgersSQL Airplane Tracker.
    Программа создает БД для самолетов находящихся в 10 странах.
    (France, Germany, Italy, Spain, Sweden, Poland, Greece, Portugal, Netherlands, Austria.)
    В реальном времени.""")

    list_country = ["France", "Germany", "Italy", "Spain", "Sweden", "Poland", "Greece", "Portugal", "Netherlands", "Austria"]

    api_1 = APICoordinates()

    result_country = []
    result_airplanes = []

    for country in list_country:
        api_1.get_response_api("Germany")
        api_1.get_coordinates()
        api_2 = APIAircraft()
        api_2.get_response_api(api_1.coordinates)
        data_air = api_2.aeroplanes
