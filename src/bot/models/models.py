
from peewee import *

SQLITE_DB_PATH = 'database/test.db'

database = SqliteDatabase(SQLITE_DB_PATH)


class BaseModel(Model):
    class Meta:
        database = database


class User(BaseModel):
    id = PrimaryKeyField(unique=True)
    chat_id = IntegerField()
    user_id = IntegerField()
    status = BooleanField(default=True)
    first_name = CharField(max_length=255)
    last_name = CharField(max_length=255)
    selected_counter = IntegerField(default=0)

    class Meta:
        db_table = "users"
        order_by = 'id'


# TODO плохая таблица, сделать с [id, type_game(f_id),user,chat,date]
class Game(BaseModel):
    id = PrimaryKeyField(unique=True)
    chat_id = IntegerField()
    user_id = IntegerField()
    date_handsome_of_day = DateField()  # default=datetime.datetime.now
    handsome_of_day = BooleanField(default=False)
    
    class Meta:
        db_table = "games"
        order_by = 'id'
