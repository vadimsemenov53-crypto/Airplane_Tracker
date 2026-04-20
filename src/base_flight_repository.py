from abc import ABC, abstractmethod
from typing import Any

class BaseFlightRepository(ABC):
    """ Базовый класс для работы с таблицами. """
    def __init__(self, table_name: str, params: dict[str, str]):
        """Метод - конструктор, для инициализации объектов класса."""
        self.table_name = table_name
        self.params = params

    @abstractmethod
    def connet(self):
        """ Метод для подключения к БД. """

    @abstractmethod
    def create_table(self):
        """ Метод для создания таблиц. """

    @abstractmethod
    def insert_flight(self, data: list[Any]):
        """ Метод добавления информации о самолетах. """