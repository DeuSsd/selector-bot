from models.models import *

def add_user_if_not_exist(chat_id, user_id):
    query = User.select(User.id).where(
        (User.chat_id == chat_id) &
        (User.user_id == user_id)
    )
    if not len(query):
        new_member = User(
            chat_id=chat_id,
            user_id=user_id
        )
        new_member.save()
        return new_member.id
    return None


def remuve_dublicate_user(chat_id, user_id):
    query = User.select(User.id).where(
        (User.chat_id == chat_id) &
        (User.user_id == user_id)
    )
    for id in query[1:]:
        User.delete_by_id(id)
        print(f"User remuved {id} chat_id = {chat_id}; user_id = {user_id}")


def remuve_user(chat_id, user_id):
    query = User.select(User.id).where(
        (User.chat_id == chat_id) &
        (User.user_id == user_id)
    )
    for id in query:
        User.delete_by_id(id)
        print(f"User remuved {id} chat_id = {chat_id}; user_id = {user_id}")


if __name__ == "__main__":
    chat_id = -553294046
    user_id = 390239427
    # remuve_dublicate_user(chat_id, user_id)
    # print(add_user_if_not_exist(chat_id, user_id))
    # remuve_user(chat_id, user_id)
