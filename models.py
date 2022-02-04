import os
from dotenv import load_dotenv
from datetime import datetime
from playhouse.mysql_ext import MySQLConnectorDatabase
from playhouse.migrate import SqliteMigrator, migrate
from peewee import (
    SqliteDatabase, 
    PostgresqlDatabase,
    Model, 
    CharField, 
    FloatField, 
    DateField, 
    PrimaryKeyField)


load_dotenv()

db_mysql = MySQLConnectorDatabase(
    os.getenv('MYSQL_DB'),
    host=os.getenv('MYSQL_HOST'),
    password=os.getenv('MYSQL_PASS'),
    user=os.getenv('MYSQL_USER')
)

db_posgre = PostgresqlDatabase(
    os.getenv('POSTGRE_DB'),
    user=os.getenv('POSTGRE_USER'),
    password=os.getenv('POSTGRE_PASS'),
    host=os.getenv('POSTGRE_HOST')
)

db = SqliteDatabase('test.db')
migrator = SqliteMigrator(db)


class BaseModels(Model):
    id = PrimaryKeyField(unique=True)

    class Meta:
        database = db
        order_by = 'id'

class Order(BaseModels):
    name = CharField()
    amount = FloatField(default=0)
    date = DateField(default=datetime.now())
    
    class Meta:
        table_name = 'orders'