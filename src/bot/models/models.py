from peewee import *

SQLLITE_DB_PATH = 'test.db'

database   = SqliteDatabase(SQLLITE_DB_PATH)


class BaseModel(Model):
    class Meta:
        database = database


class User(BaseModel):
    id = PrimaryKeyField(unique=True)
    chat_id = IntegerField()
    user_id = IntegerField()
    status = BooleanField(default=True)
    selected_counter = IntegerField(default=0)

    class Meta:
        db_table = "users"
        order_by = 'id'
