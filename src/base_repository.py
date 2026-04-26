from abc import ABC, abstractmethod
from typing import Generic, TypeVar

import psycopg2.extensions

T = TypeVar("T")


class BaseRepository(ABC, Generic[T]):
    """Базовый класс для работы с таблицами."""

    def __init__(self, connection: psycopg2.extensions.connection) -> None:
        """Метод - конструктор, для инициализации объектов класса."""
        self.conn = connection

    @abstractmethod
    def create_table(self) -> None:
        """Метод для создания таблиц."""

    @abstractmethod
    def insert_info(self, data: T) -> None:
        """Метод добавления информации в таблицу."""
