import os
from pathlib import Path
from models import *



def create_tables():
    with database:
        database.create_tables([User, Game])
        
        
if __name__ == '__main__':
    if not os.path.isfile(Path(SQLITE_DB_PATH)):
        print("create")
        create_tables()
    else:
        print("exist")
        
    