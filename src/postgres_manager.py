import psycopg2

from src.base_db_manager import BaseDBManager

class PostgresManager(BaseDBManager):
    """ Класс для подключения к БД """
    def connect(self):
        """ Метод для подключения к БД. """
        return psycopg2.connect(dbname=self.db_name, **self.params)