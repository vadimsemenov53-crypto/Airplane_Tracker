from abc import ABC, abstractmethod

class BaseDBManager(ABC):
    """ Базовый класс для работ с базами данных. """
    def __init__(self, db_name: str, params: dict[str, str]):
        """Метод - конструктор, для инициализации объектов класса."""
        self.db_name = db_name
        self.params = params

    @abstractmethod
    def connect(self):
        """ Метод для подключения к БД. """
