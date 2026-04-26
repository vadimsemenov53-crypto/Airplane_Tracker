from typing import Any

from src.base_repository import BaseRepository


class FlightRepository(BaseRepository):
    """Дочерний класс FlightRepository.
    Для создания таблиц о самолетах и странах, и добавление информации о самолетах."""

    def create_table(self) -> None:
        """Метод для создания таблиц с данными о самолетах."""
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
            );""")

    def insert_info(self, data: dict[str, Any]) -> None:
        """Метод добавления информации."""
        query = """
        INSERT INTO airplanes (
        icao24, callsign, origin_country, time_position, last_contact,
        longitude, latitude, baro_altitude, on_ground, velocity,
        true_track, vertical_rate, geo_altitude, squawk, spi, position_source
        )
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        ON CONFLICT (icao24) DO NOTHING;"""

        values = []

        for air in data["states"]:
            if air is None:
                continue

            values.append(
                (
                    air[0],
                    air[1].strip() if air[1] else None,
                    air[2],
                    air[3],
                    air[4],
                    air[5],
                    air[6],
                    air[7],
                    air[8],
                    air[9],
                    air[10],
                    air[11],
                    air[13],
                    air[14],
                    air[15],
                    air[16],
                )
            )

        with self.conn.cursor() as cur:
            cur.executemany(query, values)

        self.conn.commit()
