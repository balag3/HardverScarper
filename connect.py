from config import Config
from peewee import PostgresqlDatabase

db = PostgresqlDatabase(
    database=Config.load('database'),
    user=Config.load('user'),
    password=Config.load('password'),
    host=Config.load('host'),
)
