import time
from models import *


value_start = time.time()
list_data = [
    {"name": "Bread", "amount": 9.99},
    {"name": "Milk", "amount": 2.5},
    {"name": "Meat", "amount": 25},
    {"name": "Water", "amount": 1.5},
    {"name": "Potato", "amount": 3.70},
    {"name": "Banana", "amount": 3.33},
    {"name": "Bokoya", "amount": 5},
    {"name": "Carrot", "amount": 7.53},
    {"name": "Cucumber", "amount": 5.665},
    {"name": 'Coffee', "amount": 8.73}
] 

value_mysql = time.time()
with db_mysql:
    db.create_tables([Order])
    if not Order.select().count():
        Order.insert_many(
           list_data
        ).execute()
    list_data_mysql = Order.select()

print(f"We developed mysql table and it took {time.time()-value_mysql} seconds")
print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')

value_postgre = time.time()
with db_posgre:
    db.create_tables([Order])
    if not Order.select().count():
        Order.insert_many(
           list_data_mysql
        ).execute()
    list_data_postgre = Order.select()

print(f"We developed mysql table and it took {time.time()-value_postgre} seconds")
print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')

value_sqlite = time.time()
with db:
    db.create_tables([Order])
    if not Order.select().count():
        Order.insert_many(
           list_data_postgre
        ).execute()
    try:
        migrate(
            migrator.add_column('orders', 'name_new', CharField(default='')),
            migrator.add_column('orders', 'amount_new', FloatField(default=0)),
            migrator.add_column('orders', 'date_new', DateField(default=datetime.now()))
        )
    except:
        pass
    finally:
        print('We provided basic migration to the sqlite')
print(f"We developed mysql table and it took {time.time()-value_sqlite} seconds")
print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
print()
print(f"We developed the full work with three databases and it took {time.time()-value_start} seconds")
print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')