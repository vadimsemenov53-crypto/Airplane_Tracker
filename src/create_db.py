import psycopg2

from src.config import config
from src.base_db_manager import BaseDBManager

class CreateDB(BaseDBManager):
    """ Дочерний класс BaseDBManager.
     Для создания и удаления БД."""

    def connect(self, db_name="postgres"):
        """ Метод для подключения к БД. """
        return psycopg2.connect(dbname=db_name, **self.params)

    def create_db(self):
        """ Метод для создания БД. """
        conn = self.connect()
        conn.autocommit = True

        with conn.cursor() as cur:
            cur.execute("SELECT 1 FROM pg_database WHERE datname = %s", (self.db_name,))
            exists = cur.fetchone()

            if not exists:
                cur.execute(f"CREATE DATABASE {self.db_name}")

        conn.close()

    def drop_db(self):
        """ Метод для удаления БД. """
        conn = self.connect()
        conn.autocommit = True

        with conn.cursor() as cur:
            cur.execute(f"DROP DATABASE IF EXISTS {self.db_name}")

        conn.close()


if __name__ == '__main__':
    db = CreateDB('airplane', config())
    db.create_db()


