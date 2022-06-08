import random
from games import HandsomeOFTheDay
from models.models import *

from peewee import ModelSelect

from typing import List, Optional, TypeVar

id = TypeVar('id')


def get_fullname(user: User) -> str:
    return f"{user.first_name} {user.last_name}" if user.last_name else f"{user.first_name}"


def add_user_if_not_exist(chat_id: id, user_id: id, first_name: str, last_name: str = "") -> Optional[id]:
    query = User.select(User.id).where(
        (User.chat_id == chat_id) &
        (User.user_id == user_id)
    )
    if not len(query):
        new_member = User(
            chat_id=chat_id,
            user_id=user_id,
            first_name=first_name if first_name else "",
            last_name=last_name if last_name else ""
        )
        new_member.save()
        return new_member.id
    return None


def remove_dublicate_user(chat_id: id, user_id: id) -> None:
    query = User.select(User.id).where(
        (User.chat_id == chat_id) &
        (User.user_id == user_id)
    )
    for id in query[1:]:
        User.delete_by_id(id)
        print(f"User removed {id} chat_id = {chat_id}; user_id = {user_id}")


def remove_user(chat_id: id, user_id: id) -> bool:
    query = User.select().where(
        (User.chat_id == chat_id) &
        (User.user_id == user_id)
    )
    flag = False
    for id in query:
        flag = User.delete_by_id(id)
        print(f"User removed {id} chat_id = {chat_id}; user_id = {user_id}")

    return flag


def select_users_in_chat(chat_id: id) -> ModelSelect:
    query = User.select().where(
        (User.chat_id == chat_id) &
        (User.status == True)
    ).order_by(User.selected_counter)
    return query


def compile_message_statistics(user_selected: ModelSelect) -> str:
    # print(len(user_selected))
    msg = '🎉 Результаты Красавчик Дня\n'
    number = 1
    for user in user_selected:
        msg += f"{number}) {user.selected_counter} раз(а) - {get_fullname(user)}\n"
        number += 1
    return msg


def get_statistics(chat_id: id) -> str:
    query = select_users_in_chat(chat_id)
    return compile_message_statistics(query)


def drop_statistics(chat_id: id) -> str:
    query = select_users_in_chat(chat_id)
    for user in query:
        user.selected_counter = 0  # TODO Many insert
        user.save()
    HandsomeOFTheDay.drop_data(chat_id)
    
    return compile_message_statistics(query)


def modify_counter(user_record_id: id) -> User:
    selected_user = User.get_by_id(user_record_id)
    selected_user.selected_counter += 1
    selected_user.save()
    return selected_user


def select_random_user(user_selected: ModelSelect) -> id:
    user_poll: List[id] = []
    for user in user_selected:
        user_poll.append(user.id)
    selected_user_record_id = random.choice(user_poll)

    # print(user_poll, selected_user_record_id)
    return selected_user_record_id


def compile_message_winner(full_name: str) -> str:
    msg = f"""КРУТИМ БАРАБАН
Ищем красавчика в этом чате
Гадаем на бинарных опционах 📊
Анализируем лунный гороскоп 🌖
Лунная призма дай мне силу 💫
СЕКТОР ПРИЗ НА БАРАБАНЕ 🎯
🎉 Сегодня красавчик дня - {full_name}"""
    return msg


def randomly_choose_one_user(chat_id: id) -> str:
    if HandsomeOFTheDay.check_available_game(chat_id):
        query = select_users_in_chat(chat_id)
        selected_user_record_id = select_random_user(query)
        selected_user = modify_counter(selected_user_record_id)
        HandsomeOFTheDay.update_event(chat_id,selected_user.user_id)
        return compile_message_winner(get_fullname(selected_user))
    else:
        selected_user_id= HandsomeOFTheDay.get_user_id(chat_id)
        query = select_users_in_chat(chat_id).where(User.user_id == selected_user_id)
        assert len(query) == 1, "В таблице найдены дубликаты"
        selected_user: User = query[0]
        return f"Красавчик дня - {get_fullname(selected_user)}"

if __name__ == "__main__":
    chat_id = -553294046
    user_id = 390239427
    # remove_dublicate_user(chat_id, user_id)
    # print(add_user_if_not_exist(chat_id, user_id))
    # remove_user(chat_id, user_id)
    # select_users_in_chat(chat_id)
    print(randomly_choose_one_user(chat_id))
    print(get_statistics(chat_id))
    # for i in range(1000000):
        # randomly_choose_one_user(chat_id)
    # print(get_statistics(chat_id))
    # print(randomly_choose_one_user(chat_id).split("\n"))