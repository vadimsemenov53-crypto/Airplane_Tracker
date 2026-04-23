from typing import Any

import psycopg2.extensions

from src.config import config
from src.postgres_manager import PostgresManager


class DBManager:
    """Базовый класс для работы с данными таблицы."""

    def __init__(self, connection: psycopg2.extensions.connection) -> None:
        """Метод - конструктор, для инициализации объектов класса."""
        self.conn = connection

    def get_info_countries_and_planes(self) -> list[dict[str, int]]:
        """Метод для получения списка всех стран и количество самолётов в каждой стране."""
        with self.conn.cursor() as cur:
            cur.execute("""
            SELECT origin_country, COUNT(*)
            FROM airplanes
            GROUP BY origin_country;
            """)

            rows = cur.fetchall()

            return [{"country": country, "count": count} for country, count in rows]

    def get_all_planes(self) -> list[dict[str, Any]]:
        """Метод для получения списка всех самолётов с указанием страны регистрации,
        номера самолёта, скорость полёта и высота полёта."""
        with self.conn.cursor() as cur:
            cur.execute("""
            SELECT origin_country, icao24, velocity, baro_altitude
            FROM airplanes;
            """)

            rows = cur.fetchall()

            return [
                {"country": country, "board_number": icao24, "speed": speed, "height": height}
                for country, icao24, speed, height in rows
            ]

    def get_avg_height(self) -> float:
        """Метод для получения средней высоты полёта всех самолётов."""
        with self.conn.cursor() as cur:
            cur.execute("""
            SELECT AVG(baro_altitude)
            FROM airplanes;
            """)

            result = cur.fetchone()

            avg = result[0] if result else None

            if avg is None:
                return 0.0

            return round(float(avg), 2)

    def get_max_height(self) -> list[dict[str, Any]]:
        """Метод для получения списка всех самолётов, у которых высота полёта выше средней по всем самолётам."""
        with self.conn.cursor() as cur:
            cur.execute("""
            SELECT origin_country, icao24, velocity, baro_altitude
            FROM airplanes
            WHERE baro_altitude > (SELECT AVG(baro_altitude) FROM airplanes);;
            """)

            rows = cur.fetchall()

            return [
                {"country": country, "board_number": icao24, "speed": speed, "height": height}
                for country, icao24, speed, height in rows
            ]

    def get_planes_by_countries(self, list_country: list[str]) -> list[dict[str, Any]]:
        """Метод получает список всех самолётов, зарегистрированных в странах
        названия которых переданы в метод, например (Iran, Russia)."""
        result_list = []

        query = """
        SELECT origin_country, icao24, velocity, baro_altitude
        FROM airplanes
        WHERE origin_country = ANY(%s);
        """

        with self.conn.cursor() as cur:
            cur.execute(query, (list_country,))
            rows = cur.fetchall()

            for country_name, icao24, speed, height in rows:
                result_list.append({"country": country_name, "board_number": icao24, "speed": speed, "height": height})

        return result_list


# if __name__ == "__main__":
#     params = config()
#
#     manager = PostgresManager("airplane", params)
#     conn = manager.connect()
#
#     db_manager = DBManager(conn)
#     data = db_manager.get_planes_by_countries(["Germany", "France", "Italy"])
#     # print(data)
#
#     conn.close()
#
#     for i in data:
#         print(i)
