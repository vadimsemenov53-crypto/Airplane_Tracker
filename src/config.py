import os

from dotenv import load_dotenv


def config() -> dict[str, str]:
    """Вспомогательная функция для использования скрытых средств подключения к БД."""
    path = os.path.dirname(os.path.dirname(__file__))
    path_env = os.path.join(path, ".env")
    load_dotenv(path_env)

    db_config = {
        "user": os.getenv("POSTGRES_USER") or "",
        "password": os.getenv("POSTGRES_PASSWORD") or "",
        "host": os.getenv("POSTGRES_HOST") or "",
        "port": os.getenv("POSTGRES_PORT") or "",
    }
    return db_config
