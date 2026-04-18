import os
from dotenv import load_dotenv

def config() -> dict[str, str]:
    """ Вспомогательная функция для использования скрытых средств подключения к БД. """
    path = os.path.dirname(os.path.dirname(__file__))
    path_env = os.path.join(path, ".env")
    load_dotenv(path_env)

    db_config = {
        'user': os.getenv('POSTGRES_USER'),
        'password': os.getenv('POSTGRES_PASSWORD'),
        'host': os.getenv('POSTGRES_HOST'),
        'port': os.getenv('POSTGRES_PORT')
    }
    return db_config

print(config())