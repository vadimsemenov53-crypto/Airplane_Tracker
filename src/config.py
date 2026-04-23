import os

from dotenv import load_dotenv

from src.db_params import DBParams


def config() -> DBParams:
    """Вспомогательная функция для использования скрытых средств подключения к БД."""
    path = os.path.dirname(os.path.dirname(__file__))
    path_env = os.path.join(path, ".env")
    load_dotenv(path_env)

    db_config: DBParams = {
        "user": get_env("POSTGRES_USER"),
        "password": get_env("POSTGRES_PASSWORD"),
        "host": get_env("POSTGRES_HOST"),
        "port": get_env("POSTGRES_PORT"),
    }
    return db_config


def get_env(name: str) -> str:
    """Вспомогательная функция для типизации config."""
    value = os.getenv(name)
    if value is None:
        raise ValueError(f"{name} не задан")
    return value
