from models import *


if __name__ == "__main__":
    with db:
        db.create_tables([User])
