from typing import Any

from src.base_repository import BaseRepository


class CountryRepository(BaseRepository):
    """Дочерний класс FlightRepository.
    Для создания таблиц о странах, и добавление информации о них."""

    def create_table(self) -> None:
        """Метод для создания таблиц."""
        self.conn.autocommit = True

        with self.conn.cursor() as cur:
            cur.execute("""CREATE TABLE IF NOT EXISTS country (
            place_id INT PRIMARY KEY,
            osm_type VARCHAR(30),
            osm_id INT,
            lat DOUBLE PRECISION NOT NULL,
            lon DOUBLE PRECISION NOT NULL,
            class VARCHAR(30),
            type VARCHAR(30),
            place_rank INT,
            importance DOUBLE PRECISION,
            addresstype VARCHAR(30),
            name VARCHAR(100) NOT NULL,
            display_name TEXT NOT NULL
            );""")

    def insert_info(self, data: list[dict[str, Any]]) -> None:
        """Метод добавления информации в таблицу."""
        query = """
        INSERT INTO country (
        place_id , osm_type, osm_id, lat, lon, class, type, place_rank, importance, addresstype, name, display_name
        )
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
        """

        values = []

        for item in data:
            values.append(
                (
                    item.get("place_id"),
                    item.get("osm_type"),
                    item.get("osm_id"),
                    float(item.get("lat")),
                    float(item.get("lon")),
                    item.get("class"),
                    item.get("type"),
                    item.get("place_rank"),
                    item.get("importance"),
                    item.get("addresstype"),
                    item.get("name"),
                    item.get("display_name"),
                )
            )

        with self.conn.cursor() as cur:
            cur.executemany(query, values)

        self.conn.commit()


if __name__ == "__main__":
    from src.api_client import APICoordinates
    from src.config import config
    from src.postgres_manager import PostgresManager

    api_1 = APICoordinates()
    api_1.get_response_api("Germany")
    data_country = api_1._data_response

    params = config()

    manager2 = PostgresManager("airplane", params)
    conn2 = manager2.connect()

    table = CountryRepository(conn2)
    table.insert_info(data_country)

    conn2.close()
