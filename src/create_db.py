from src.config import config
from src.postgres_manager import PostgresManager

class CreateDB:
    """ Класс для создания и удаления БД."""

    def __init__(self, connection):
        """Метод - конструктор, для инициализации объектов класса."""
        self.conn = connection

    def create_db(self, db_name: str):
        """ Метод для создания БД. """
        self.conn.autocommit = True

        with self.conn.cursor() as cur:
            cur.execute("SELECT 1 FROM pg_database WHERE datname = %s", (db_name,))
            exists = cur.fetchone()

            if not exists:
                cur.execute(f"CREATE DATABASE {db_name}")

    def drop_db(self, db_name: str):
        """ Метод для удаления БД. """
        self.conn.autocommit = True

        with self.conn.cursor() as cur:
            cur.execute(f"DROP DATABASE IF EXISTS {db_name}")


if __name__ == '__main__':
    params = config()
    ex_1 = PostgresManager('postgres', params)
    db = CreateDB(ex_1.connect())
    db.drop_db('airplane')


