from abc import ABC, abstractmethod
from typing import Any

class BaseFlightRepository(ABC):
    """ Базовый класс для работы с таблицами. """
    def __init__(
            self,
            connection,
            data_airplane: dict[str, Any]
    ) -> None:
        """Метод - конструктор, для инициализации объектов класса."""
        self.conn = connection
        self.data_airplane = data_airplane

    @abstractmethod
    def create_table(self) -> None:
        """ Метод для создания таблиц. """

    @abstractmethod
    def insert_info(self, data: list[Any]) -> None:
        """ Метод добавления информации. """