import psycopg2
import os
from dotenv import load_dotenv

path = os.path.dirname(os.path.dirname(__file__))
path_env = os.path.join(path, ".env")
load_dotenv(path_env)

