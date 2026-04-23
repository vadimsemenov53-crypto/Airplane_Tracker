from typing import TypedDict


class DBParams(TypedDict):
    """Класс типизации параметров подключения."""

    user: str
    password: str
    host: str
    port: str
