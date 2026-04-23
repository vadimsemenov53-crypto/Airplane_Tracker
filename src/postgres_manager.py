import psycopg2
from psycopg2.extensions import connection

from src.db_params import DBParams


class PostgresManager:
    """Класс для подключения к БД."""

    def __init__(self, db_name: str, params: DBParams):
        """Метод - конструктор, для инициализации объектов класса."""
        self.db_name = db_name
        self.params = params

    def connect(self) -> connection:
        """Метод для подключения к БД."""
        return psycopg2.connect(
            dbname=self.db_name,
            user=self.params["user"],
            password=self.params["password"],
            host=self.params["host"],
            port=self.params["port"],
        )
