from peewee import *

SQLLITE_DB_PATH = 'test.db'

db = SqliteDatabase(SQLLITE_DB_PATH)


class BaseModel(Model):
    id = PrimaryKeyField(unique=True)

    class Meta:
        database = db
        order_by = 'id'


class User(BaseModel):
    user_id = IntegerField()
    status = BooleanField(default=True)
    selected_counter = IntegerField(default=0)

    class Meta:
        db_table = "users"
