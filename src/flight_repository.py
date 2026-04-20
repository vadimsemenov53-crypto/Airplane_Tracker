from src.base_flight_repository import BaseFlightRepository
from typing import Any

from src.config import config
from src.postgres_manager import PostgresManager
from src.create_db import CreateDB

class FlightRepository(BaseFlightRepository):
    """ Дочерний класс FlightRepository.
     Для создания таблиц о самолетах и странах, и добавление информации о самолетах."""

    def create_table(self) -> None:
        """ Метод для создания таблиц с данными о самолетах. """
        self.conn.autocommit = True

        with self.conn.cursor() as cur:
            cur.execute("""CREATE TABLE IF NOT EXISTS airplanes (
            icao24 VARCHAR(30) PRIMARY KEY,
            callsign VARCHAR(50),
            origin_country VARCHAR(100) NOT NULL,
            time_position BIGINT,
            last_contact BIGINT,
            longitude DOUBLE PRECISION,
            latitude DOUBLE PRECISION,
            baro_altitude DOUBLE PRECISION,
            on_ground BOOLEAN,
            velocity DOUBLE PRECISION,
            true_track DOUBLE PRECISION,
            vertical_rate DOUBLE PRECISION,
            geo_altitude DOUBLE PRECISION,
            squawk VARCHAR(50),
            spi BOOLEAN,
            position_source INT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )""")

    def insert_info(self, data: list[Any]) -> None:
        """ Метод добавления информации. """


if __name__ == '__main__':
    params = config()

    manager = PostgresManager('postgres', params)
    conn = manager.connect()

    db = CreateDB(conn)
    db.drop_db('airplane')
    conn.close()
    #
    # manager2 = PostgresManager('airplane', params)
    # conn2 = manager2.connect()
    #
    # table = FlightRepository(conn2)
    # table.create_table()
    # conn2.close()
