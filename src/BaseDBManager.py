from abc import ABC, abstractmethod

class BaseDBManager(ABC):
    """ Базовый класс для работ с базами данных. """
    def __init__(self, params: dict[str, str]):
        self.params = params

    @abstractmethod
    def connect(self, db_name: str):
        """ Метод для подключения к БД. """
