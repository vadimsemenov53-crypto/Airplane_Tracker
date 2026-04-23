from interface.utils_app import ask_user, iterator, show_message, writing_api_to_tables
from src.config import config
from src.country_repository import CountryRepository
from src.create_db import CreateDB
from src.db_manager import DBManager
from src.flight_repository import FlightRepository
from src.postgres_manager import PostgresManager


def run_app() -> None:
    """Основная функция для работы программы."""

    show_message("""Запуск PostgersSQL Airplane Tracker.
    Программа создает БД для самолетов находящихся в 10 странах.
    (France, Germany, Italy, Spain, Sweden, Poland, Greece, Portugal, Netherlands, Austria.)
    В реальном времени.
    Выполнение замедленно специально, для избежание превышения количества запросов.
    1 запрос - 2 секунды.""")

    params = config()

    manager_1 = PostgresManager("postgres", params)
    conn_1 = manager_1.connect()

    db = CreateDB(conn_1)
    db.create_db("airplane")
    conn_1.close()

    manager_2 = PostgresManager("airplane", params)
    conn_2 = manager_2.connect()

    country_repo = CountryRepository(conn_2)
    country_repo.create_table()

    flight_repo = FlightRepository(conn_2)
    flight_repo.create_table()

    writing_api_to_tables(country_repo, flight_repo)

    db_manager = DBManager(conn_2)

    while True:
        show_message("""Данные готовы и записаны в БД.
        Вам доступны следующие действия:
        1- список стран и кол-во от каждой.
        2- данные о регистрации, номерах, скорости и высоте всех самолетов.
        3- расчет средней высоты полета.
        4- список бортов, летящих выше среднего показателя.
        5- поиск самолетов по конкретным названиям стран (например, Iran, Russia).
        6- выход из программы.
        Передайте цифру для вывода информации.""")
        try:
            choice = int(ask_user())

            if choice == 1:
                iterator(db_manager.get_info_countries_and_planes())

            elif choice == 2:
                iterator(db_manager.get_all_planes())

            elif choice == 3:
                avg = db_manager.get_avg_height()
                print(f"Средняя высота полета всех самолетов = {avg}")

            elif choice == 4:
                iterator(db_manager.get_max_height())

            elif choice == 5:
                show_message("""Передайте через запятую названия стран для поиска (Iran, Russia)""")
                user_input = ask_user()
                list_country = [c.strip() for c in user_input.split(",") if c.strip()]

                iterator(db_manager.get_planes_by_countries(list_country))

            elif choice == 6:
                show_message("Завершение работы программы.")
                conn_2.close()
                break

            else:
                show_message("Передано неверное значение.")

        except ValueError:
            show_message("Введите число от 1 до 6")
            continue
