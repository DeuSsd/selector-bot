from models import *


def create_tables():
    with database:
        database.create_tables([User, Game])
        
        
if __name__ == '__main__':
    create_tables()
    