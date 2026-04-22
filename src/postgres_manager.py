import psycopg2

class PostgresManager:
    """ Класс для подключения к БД. """
    def __init__(self, db_name: str, params: dict[str, str]):
        """Метод - конструктор, для инициализации объектов класса."""
        self.db_name = db_name
        self.params = params

    def connect(self):
        """ Метод для подключения к БД. """
        return psycopg2.connect(dbname=self.db_name, **self.params)