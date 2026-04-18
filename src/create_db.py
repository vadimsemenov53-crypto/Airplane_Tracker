import psycopg2

from src.config import config

def create_database(db_name: str, params: dict):
    """ Вспомогательная функция для создания базы данных. """
    conn = psycopg2.connect(dbname="postgres", **params)
    conn.autocommit = True
    cur = conn.cursor()

    cur.execute(f"SELECT 1 FROM pg_database WHERE datname = '{db_name}'")
    exists = cur.fetchone()

    if not exists:
        cur.execute(f"CREATE DATABASE {db_name}")

    cur.close()
    conn.close()


def drop_database(db_name: str, params: dict):
    pass

if __name__ == '__main__':
    create_database('airplane', config())


