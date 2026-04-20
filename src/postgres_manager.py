import psycopg2

from src.base_db_manager import BaseDBManager

class PostgresManager(BaseDBManager):
    """ Класс для подключения к БД """
    def connect(self, db_name="postgres"):
        """ Метод для подключения к БД. """
        return psycopg2.connect(dbname=db_name, **self.params)