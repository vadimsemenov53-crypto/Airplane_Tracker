from abc import ABC, abstractmethod
from typing import Any

import psycopg2.extensions


class BaseRepository(ABC):
    """Базовый класс для работы с таблицами."""

    def __init__(self, connection: psycopg2.extensions.connection) -> None:
        """Метод - конструктор, для инициализации объектов класса."""
        self.conn = connection

    @abstractmethod
    def create_table(self) -> None:
        """Метод для создания таблиц."""

    @abstractmethod
    def insert_info(self, data: dict[str, Any]) -> None:
        """Метод добавления информации в таблицу."""
