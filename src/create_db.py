import psycopg2.extensions


class CreateDB:
    """Класс для создания и удаления БД."""

    def __init__(self, connection: psycopg2.extensions.connection) -> None:
        """Метод - конструктор, для инициализации объектов класса."""
        self.conn = connection

    def create_db(self, db_name: str) -> None:
        """Метод для создания БД."""
        self.conn.autocommit = True

        with self.conn.cursor() as cur:
            cur.execute("SELECT 1 FROM pg_database WHERE datname = %s", (db_name,))
            exists = cur.fetchone()

            if not exists:
                cur.execute(f"CREATE DATABASE {db_name}")

    def drop_db(self, db_name: str) -> None:
        """Метод для удаления БД."""
        self.conn.autocommit = True

        with self.conn.cursor() as cur:
            cur.execute(f"DROP DATABASE IF EXISTS {db_name}")
